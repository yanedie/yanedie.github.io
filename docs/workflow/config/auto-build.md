---
created: 2023-09-16T18:54
tags: []
source: http://clifford.vip/More/mkdocs%E7%9F%A5%E8%AF%86%E5%BA%93/
author: 百里
updated: 2024-07-09T23:10
---
## 自动构建知识库

**MkDocs+Jenkins+Gitee+Nginx**

实现效果：当代码推送到笔记仓库后，立即触发 Jenkins 构建任务，并发布笔记到云服务器上。

适用场景：

- 个人知识库
- 技术分享
- 简历加分

## 准备

**流程**

![](http://clifford.vip/More/assets/2022-05-16-22-31-57.png)

![](http://clifford.vip/More/assets/2022-05-16-22-02-18.png)

**服务器**

- 服务商：腾讯云轻量级服务器
- ip:114.132.62.78
- 版本：Ubuntu20.04

如果是腾讯云的 ubuntu20.04，需要先执行以下准备工作：

```
# 初始化root用户
$ sudo passwd root

# 开启ssh远程访问
$ echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
$ sudo service ssh restart

```

**添加新用户**

本文默认都是使用 cifer 用户进行操作。

```
# 添加用户
sudo adduser cifer

# 添加到sudo组
sudo usermod -aG sudo cifer

# 切换用户
su cifer

```

**Gitee 仓库**

自己创建一个专门存放笔记的项目仓库。

## Python3

apt 工具包更新后自带 Python3.8.10

```
# 更新本地包
sudo apt update

# 检查python版本
python3 -V

```

安装 mkdocs 相关依赖

- mkdocs
- mkdocs-material

```
# 安装virtualenv
$ apt install python3-virtualenv

# 创建虚拟环境
$ mkdir ~/envs
$ cd ~/envs
$ virtualenv mk

# 激活虚拟环境
$ source ~/envs/mk/bin/activate

# 安装mkdocs
$ pip install mkdocs
# 检查mkdocs版本
$ mkdocs -V

# 安装mkdocs-material
$ pip install mkdocs-material

```

备注：如果安装库网速慢，可以给`pip install`加上豆瓣镜像选项，例如：

```
pip install mkdocs -i https://pypi.douban.com/simple

```

mkdocs的配置文件`mkdocs.yml`:

```
site_name: 百里测试小站
site_description: 百里测试小站
site_author: 百里

theme:
  name: material
markdown_extensions:
  - attr_list
  - admonition
  - toc:
      permalink: true
  - pymdownx.tasklist:
      custom_checkbox: true

```

## Java11

```
# 安装openjdk
$ apt install openjdk-11-jdk

# 检查安装结果
$ java -version

```

记住 Java 可执行文件路径：`/usr/lib/jvm/java-11-openjdk-amd64`，后面配置 Jenkins 代理节点需要。

## Docker

预备依赖

```
# 更新本地包
$ sudo apt update

# 安装必要的一些依赖
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common

# 为Docker仓库添加GPG key：
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 把Docker仓库添加到APT源：
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

# 安装docker
$ sudo apt install docker-ce

# 验证安装结果
$ docker --version

# 添加分组（避免每次输入sudo）
$ sudo usermod -aG docker cifer

# 切换用户（这时需要输入密码）
$ su - cifer

# 检查权限（预期：cifer sudo docker）
$ groups

```

## Nginx

```
# 初始化挂载目录
$ mkdir -p ~/nginx_mount/conf
$ mkdir -p ~/nginx_mount/html
$ mkdir -p ~/nginx_mount/logs

# 修改目录权限（以便mkdocs生成的资源可以拷贝覆盖其中）
$ chmod 777 ~/nginx_mount/html

# 添加配置文件
$ vi ~/nginx_mount/conf/nginx.conf

```

配置信息内容，并保存。

```
events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page  404              /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}

```

启动 nginx 容器：

```
# 启动Nginx容器
$ docker run -d --name nginx-cifer -p 80:80 -v ~/nginx_mount/conf/nginx.conf:/etc/nginx/nginx.conf -v ~/nginx_mount/html:/etc/nginx/html -v ~/nginx_mount/logs:/var/log/nginx nginx

```

备注：记得在云服务器中的安全组（阿里云）/防火墙（腾讯云）中开放`80`端口。

## Jenkins

### 1 运行容器

```
cd ~

# 初始化挂载目录
$ mkdir jenkins_mount

# 修改权限
$ chmod 777 jenkins_mount

# 启动Jenkins容器
$ docker run -d -p 8080:8080 -p 50000:50000 -v $PWD/jenkins_mount:/var/jenkins_home --name jenkins-cifer jenkins/jenkins:lts

# 查看容器运行情况
$ docker ps

```

备注：记得在云服务器中的安全组（阿里云）/防火墙（腾讯云）中开放以上端口。

### 2 初始化

> 访问地址：[http://114.132.62.78:8080/](http://114.132.62.78:8080/)

- 解锁 Jenkins

获取管理员密码：

```
# 查询Jenkins解锁密码
$ cat ~/jenkins_mount/secrets/initialAdminPassword

```

解释：因为是容器，所以用容器挂载目录～/jenkins\_mount 替换/var/jenkins\_home 即可。

![](http://clifford.vip/More/assets/2022-05-16-22-05-05.png)

- 初始化插件

![](http://clifford.vip/More/assets/2022-05-16-22-05-15.png)

添加用户 ![](http://clifford.vip/More/assets/2022-05-16-22-05-39.png)

### 3 安装插件[¶](http://clifford.vip/More/mkdocs%E7%9F%A5%E8%AF%86%E5%BA%93/#3 "Permanent link")

- Gitee：用来实现 WebHook 触发构建

    > 菜单路径：[http://114.132.62.78:8080/pluginManager/](http://114.132.62.78:8080/pluginManager/)

![](http://clifford.vip/More/assets/2022-05-16-22-06-08.png)

### 4 添加代理[¶](http://clifford.vip/More/mkdocs%E7%9F%A5%E8%AF%86%E5%BA%93/#4 "Permanent link")

> 菜单路径：[http://114.132.62.78:8080/computer/](http://114.132.62.78:8080/computer/)

- 新建节点

![](http://clifford.vip/More/assets/2022-05-16-22-06-35.png)

![](http://clifford.vip/More/assets/2022-05-16-22-06-46.png)

- 配置代理节点

绑定 Ubuntu20.04 宿主机作为节点，用来实际执行 python3 脚本。

- 启动代理

![](http://clifford.vip/More/assets/2022-05-16-22-23-54.png)

如果日志提示：`Agent successfully connected and online`，则表示代理节点启动成功。

代理节点正常时的节点列表状态： ![](http://clifford.vip/More/assets/2022-05-16-22-24-11.png)

### 5 创建任务[¶](http://clifford.vip/More/mkdocs%E7%9F%A5%E8%AF%86%E5%BA%93/#5 "Permanent link")

![](http://clifford.vip/More/assets/2022-05-16-22-24-22.png)

- 面板：General

- 限制项目的运行节点

标签表达式：填入代理节点的名称，例如`tencent-ubuntu`

- **面板：源码管理**

- Git

|

- **面板：构建触发器**
- Gitee webhook 触发构建

备注：此选项只有在 Jenkins 安装了 Gitee 插件后才可以使用。

> 生成密码后，可以进入 Gitee 仓库的管理菜单中，进行 webhook 的配置： URL：当前选项自动生成的地址 WebHook 密码：当前生成的密码串 选择事件： Push

- **面板：构建**

选择：执行 shell

```
#!/bin/bash

# 激活虚拟环境
source /home/cifer/envs/mk/bin/activate

# 构建项目
mkdocs build

# 修改文件权限
chmod 777 site/*

# 拷贝到nginx目录
cp -r ~/jenkins_mount/workspace/testie-notes/site/. ~/nginx_mount/html/

```

备注：`testie-notes`为 Jenkins 的 job 名称。

如果非虚拟环境，则加上python3 -m 来执行：

到此，任务已经配置完毕，可以尝试手工触发执行 job，验证构建结果是否成功。
