import xml.etree.ElementTree as ET
import os
import re
import requests
from datetime import datetime
from lxml import etree

def define_env(env):
    @env.macro
    def getErrorDict(tsPath):
        if not os.path.isfile(tsPath):
            raise ValueError("文件路径无效，请使用正斜杠（/）或文件不存在。")

        tree = ET.parse(tsPath)
        root = tree.getroot()

        promptList = [] # 提示文字列表
        solutionList = [] # 解决方案列表
        hexStrList = [] # 含有 16 进制代码的字符串列表
        hexList = [] # 纯 16 进制代码列表
        invalidHexList = [] # 不符合长度的 16 进制代码列表
        errorCode = [] # 全部错误码列表
        commonCode = [] #公共错误码列表

        # 16 进制代码正则表达式
        pattern = r'0x[0-9a-fA-F]+'

        # 提取所有<message>标签下<source>标签内的文本，并添加到列表。
        hexStr = [item[0].text for item in root.find("context").findall("message")]
        try:
                hexStrList = [(hexStr[i], hexStr[i+1], hexStr[i+2]) for i in range(0, len(hexStr), 3)]
        except IndexError:
                # 每个错误码由 3 对标签组成，初步验证是否错误码缺少标签。
                raise ValueError("无法按照步长为 3 提取 错误码的 16 进制代码。可能是错误码缺少标签。")

        # 检查 16 进制代码长度
        def checkHexLength(hexValue):
            # 长度不等于 10 位，添加到无效列表里
            if len(hexValue.group()) != 10:
                invalidHexList.append((hexValue.group()))

        # 根据正则匹配到错误码对应标签内含有 16 进制代码的字符串。
        for index, (hexStr1, hexStr2, hexStr3) in enumerate(hexStrList, start=1):
            hexValue1 = re.search(pattern, hexStr1)
            hexValue2 = re.search(pattern, hexStr2)
            hexValue3 = re.search(pattern, hexStr3)

            if hexValue1:
                checkHexLength(hexValue1)
            if hexValue2:
                checkHexLength(hexValue2)
            if hexValue3:
                checkHexLength(hexValue3)

            # 如果 16 进制代码长度没问题，但缺少的标签数量正是 3 的倍数，即通过了初步验证，那么再次验证每 3 个标签 16 进制代码是否相同。
            if hexValue1.group() == hexValue2.group() == hexValue3.group():
                hexList.append(hexValue1.group())
            else:
                # 由于依赖顺序判定，如果一处不同，后续都会不同，因此不输出所有不相等的 16 进制代码。只要知道 ts 文件缺少标签就行。
                raise ValueError(f"错误码标签的 16 进制代码不相等，首次判断为 {hexValue1.group()}, {hexValue2.group()}, {hexValue3.group()}，可能是缺少错误码标签或 16 进制代码长度与其它不同。")

        # 抛出异常 输出所有不符合长度的 16 进制代码列表。
        if invalidHexList:
                raise ValueError(f"错误码 {invalidHexList} 长度不满足 10 位。")

        # 获取问题描述文本并存入列表
        for index in range(0, len(root.find("context").findall("message")), 3):
            promptText = root.find("context").findall("message")[index][1].text
            promptList.append(promptText)

        # 获取解决方案文本并存入列表
        for index in range(2, len(root.find("context").findall("message")), 3):
            solution = root.find("context").findall("message")[index][1].text
            solutionList.append(solution)

        # 将 16 进制代码、问题描述和解决方案三个一组存为字典嵌套在列表里。
        lists = [hexList, promptList, solutionList]
        for i in range(len(lists[0])):
            errorDict = {key: lists[j][i] for j, key in enumerate(["hexCode", "prompt", "solution"])}
            errorCode.append(errorDict)

        # 提取公共错误码，16 进制代码第五第六位 00 代表公共错误码
        for item in errorCode:
            hexCode = item["hexCode"]
            if hexCode[4:6] == "00":
                commonCode.append(item)

        # 返回全部错误码和通用错误码
        return errorCode, commonCode

    @env.macro
    # 获取指定设备错误码列表
    def getDeviceDict(tsPath, nameIdx):
        # 调用函数，只获取全部错误码
        errorCode, _ = getErrorDict(tsPath)
        deviceDict = []
        # 遍历全部错误码列表内每个字典的 16 进制代码
        for item in errorCode:
            hexCode = item["hexCode"]
            # 如果 16 进制代码第五第六位和传入的参数一致，存入列表
            if hexCode[4:6] == nameIdx:
                deviceDict.append(item)
        return deviceDict

    # 标点转换过滤器，因为 ts 内都是英文标点。
    @env.filter
    def replPunctua(text):
        punctuation_map = {
            ',': '，',
            '.': '。',
            '?': '？',
            '!': '！',
            ':': '：',
            ';': '；',
            '(': '（',
            ')': '）',
        }
        return ''.join(punctuation_map.get(char, char) for char in text)

    @env.macro
    def xjh():
        base_url = 'http://fjrclh.fzu.edu.cn/cms/xjh?page={}&flag=0&searchtext='
        session = requests.session()
        # Define the range of pages to iterate through
        start_page = 1
        end_page = 20

        info = []

        for page in range(start_page, end_page + 1):
            # Build the URL for the current page
            url = base_url.format(page)
            response = session.get(url)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                html = response.text
                root = etree.HTML(html)
                comp = root.xpath("//div[@class='xjhinfo']")
                addr_date = root.xpath("//span[@class='xjhtype']//span")
                strings_to_remove = ["专场", "宣讲会", "空中", "招聘会", "校园招聘","2024","全国","福州大学","福大","届"]
                pattern = "|".join(re.escape(s) for s in strings_to_remove)

                for i in range(0, len(addr_date), 2):
                    xjh = comp[i // 2].text.strip()
                    company = re.sub(pattern, "", xjh)
                    address = addr_date[i].text.strip()
                    date = addr_date[i + 1].text.strip()
                    date_part, time_range = date.split(' ')
                    start_time, end_time = time_range.split('-')

                    # Parse date and time with the local timezone
                    start_datetime = (datetime.strptime(date_part + ' ' + start_time, "%Y.%m.%d %H:%M"))
                    end_datetime = (datetime.strptime(date_part + ' ' + end_time, "%Y.%m.%d %H:%M"))
                    # 提取开始时间和结束时间的小时和分钟部分
                    start_time_only = start_datetime.time()
                    end_time_only = end_datetime.time()

                    # 格式化时间为字符串
                    formatted_start_time = start_time_only.strftime("%H:%M")
                    formatted_end_time = end_time_only.strftime("%H:%M")

                    info.append({'公司': company, '地点': address, '日期': date_part, '开始时间': formatted_start_time, '结束时间': formatted_end_time})
            else:
                print(f"Failed to fetch page {page}. Status code: {response.status_code}")
                break  # 中止爬取
        return info