---
comments: true
created: 2023-09-21T06:27
updated: 2023-09-27T15:00
---
# 错误码

### 原理

封装一个使用 Python ElementTree 模块的函数来获取 XML 标签内的文本，并返回包含全部错误码和通用错误码的列表。利用 macros 插件，将函数注册为宏，在 Markdown 中调用函数来获得列表。结合 Jinja 的循环语法使用方括号[]运算符或者点语法取值。这样可以做到替换错误码文件即可生成错误码文档，且样式可以自由编辑。

=== "错误码文件（error_code.ts）"

	```
	<!DOCTYPE TS><TS version="2.1" language="zh_CN">
	<context>
		<name>{"1": "DEVICE_SUB_TYPE_PRO", "2": "DEVICE_SUB_TYPE_PRO_PLUS", "3": "DEVICE_SUB_TYPE_S15", "5": "DEVICE_SUB_TYPE_S20", "6": "DEVICE_SUB_TYPE_S2PLUS", "7": "DEVICE_SUB_TYPE_STOUP", "8": "DEVICE_SUB_TYPE_E3_HX", "9": "DEVICE_SUB_TYPE_E3_H", "10": "DEVICE_SUB_TYPE_E10", "11": "DEVICE_SUB_TYPE_UE", "12": "DEVICE_SUB_TYPE_UE_PRO", "13": "DEVICE_SUB_TYPE_UE_EP", "14": "DEVICE_SUB_TYPE_UE_TRIO", "15": "DEVICE_SUB_TYPE_UE_COMBO"}</name>
		<message>
			<source>EC_CalibrateInit_BoardError-0x3600ff01-prompttext</source>
			<translation>标定板数据错误.</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_BoardError-0x3600ff01-problemdescription</source>
			<translation>标定板文件错误</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_BoardError-0x3600ff01-solution</source>
			<translation>请联系技术支持</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_CamParamError-0x3600ff02-prompttext</source>
			<translation>标定数据错误.</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_CamParamError-0x3600ff02-problemdescription</source>
			<translation>相机内外参数据错误</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_CamParamError-0x3600ff02-solution</source>
			<translation>请联系技术支持</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_LaserParamError-0x3600ff03-prompttext</source>
			<translation>激光标定数据错误!</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_LaserParamError-0x3600ff03-problemdescription</source>
			<translation>光平面标定数据错误</translation>
		</message>
		<message>
			<source>EC_CalibrateInit_LaserParamError-0x3600ff03-solution</source>
			<translation>请联系技术支持</translation>
		</message>
		<message>
			<source>EC_Laser7_CalibrateError05-0x36000707-prompttext</source>
			<translation>七线激光线标定失败.</translation>
		</message>
		<message>
			<source>EC_Laser7_CalibrateError05-0x36000707-problemdescription</source>
			<translation>激光线7线标定失败。加密出现问题</translation>
		</message>
		<message>
			<source>EC_Laser7_CalibrateError05-0x36000707-solution</source>
			<translation>请重试,若连续多次失败,请联系技术支持</translation>
		</message>
		<message>
			<source>EC_UnkonwError-0x3600ffff-prompttext</source>
			<translation>未知错误.</translation>
		</message>
		<message>
			<source>EC_UnkonwError-0x3600ffff-problemdescription</source>
			<translation>未知错误</translation>
		</message>
		<message>
			<source>EC_UnkonwError-0x3600ffff-solution</source>
			<translation>请联系技术支持</translation>
		</message>
		<message>
			<source>Sn3DCalibAlgPoseTrackerError-0x34010101-prompttext</source>
			<translation>标定位姿计算 跟踪标志点失败!</translation>
		</message>
		<message>
			<source>Sn3DCalibAlgPoseTrackerError-0x34010101-problemdescription</source>
			<translation>标志点跟踪失败</translation>
		</message>
		<message>
			<source>Sn3DCalibAlgPoseTrackerError-0x34010101-solution</source>
			<translation>请将设备对准标志点</translation>
		</message>
		<message>
			<source>Sn3DCalibAlgPoseIllegalInput-0x34010102-prompttext</source>
			<translation>标定位姿计算 非法输入.</translation>
		</message>
		<message>
			<source>Sn3DCalibAlgPoseIllegalInput-0x34010102-problemdescription</source>
			<translation>标志点跟踪算法非法输入</translation>
		</message>
		<message>
			<source>Sn3DCalibAlgPoseIllegalInput-0x34010102-solution</source>
			<translation>确认算法初始化正确</translation>
		</message>
	</context>
	</TS>
	```

=== "main.py"

	```
	import xml.etree.ElementTree as ET
	import os
	import re

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

		# 提取所有  <message>标签下 <source>标签内的文本，并添加到列表。
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

	# 标点转换过滤器，因为错误码文件内都是英文标点。
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
	```

=== "markdown"

    ```
    {% raw %}
    <style>
    .foo {width: 250px !important;color: black;background-color: transparent;border-top: 0 !important;}
    tr:hover,tr:nth-child(even) {background-color:transparent !important;}
    table {border: 0 !important;}
    h2 {margin: 0 !important;padding: 0 !important;font-size: 0 !important;visibility: hidden;}
    </style>
    <!-- getErrorDict 函数第一个返回值，是一个包含 ts 文件内全部错误码的列表 -->
    {% set errorCode = 0 %}
    <!-- getErrorDict 函数第二个函数返回值，是一个包含 ts 文件内通用错误码的列表 -->
    {% set commodeCode = 1 %}
    <!-- 错误码文件所在路径 -->
    {% set tsPath = "./docs/assets/error_codes/error_code.ts" %}
    <!-- 在引号内填入代表设备型号的 16 进制代码第五位和第六位 -->
    {% set nameIdx = "01" %}

    # 错误码

    <!-- 公共错误码 -->
    {% for error in getErrorDict(tsPath)[commodeCode] %}

    ## {{ error.hexCode }}

    <div class="grid cards" markdown>
    -   :simple-hackthebox: **{{ error.hexCode }}**

        ---
        | 问题描述 { .foo } | 解决方案 { .foo } |
        | --- | --- |
        | {{ error.prompt | replPunctua }} { .foo } | {{ error.solution | replPunctua }} { .foo }  |
    </div>
    {% endfor %}

    ---

    <!-- 指定型号错误码 -->
    {% for custom in getDeviceDict(tsPath, nameIdx) %}

    ## {{ custom.hexCode }}

    <div class="grid cards" markdown>
    -   :simple-hackthebox: **{{ custom.hexCode }}**

        ---
        | 问题描述 { .foo } | 解决方案 { .foo } |
        | --- | --- |
        | {{ custom.prompt | replPunctua }} { .foo } | {{ custom.solution | replPunctua }} { .foo }  |
    </div>
    {% endfor %}
    {% endraw %}
    ```

### 渲染结果

<style>
  .foo {width: 250px !important;color: black;background-color: transparent;border-top: 0 !important;}
  tr:hover,tr:nth-child(even) {background-color:transparent !important;}
  table {border: 0 !important;}
  h2 {margin: 0 !important;padding: 0 !important;font-size: 0 !important;visibility: hidden;}
</style>

<!-- getErrorDict 函数第一个返回值，是一个包含 ts 文件内全部错误码的列表 -->
{% set errorCode = 0 %}
<!-- getErrorDict 函数第二个函数返回值，是一个包含 ts 文件内通用错误码的列表 -->
{% set commodeCode = 1 %}
<!-- 错误码文件所在路径 -->
{% set tsPath = "./docs/assets/error_codes/error_code.ts" %}
<!-- 在引号内填入代表设备型号的 16 进制代码第五位和第六位 -->
{% set nameIdx = "01" %}

<!-- 公共错误码 -->
{% for error in getErrorDict(tsPath)[commodeCode] %}

## {{ error.hexCode }}

<div class="grid cards" markdown>
-   :simple-hackthebox: **{{ error.hexCode }}**

    ---
    | 问题描述 { .foo } | 解决方案 { .foo } |
    | --- | --- |
    | {{ error.prompt | replPunctua }} { .foo } | {{ error.solution | replPunctua }} { .foo }  |
</div>
{% endfor %}

---

<!-- 指定型号错误码 -->
{% for custom in getDeviceDict(tsPath, nameIdx) %}

## {{ custom.hexCode }}

<div class="grid cards" markdown>
-   :simple-hackthebox: **{{ custom.hexCode }}**

    ---
    | 问题描述 { .foo } | 解决方案 { .foo } |
    | --- | --- |
    | {{ custom.prompt | replPunctua }} { .foo } | {{ custom.solution | replPunctua }} { .foo }  |
</div>
{% endfor %}
