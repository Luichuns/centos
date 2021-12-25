# -*- coding: utf-8 -*-
# Python 2.X版本必须添加的开头

# luichun

import os
# 导入系统操作库
import time
# 导入时间暂停库

# 第一步
# 备份华为云原来服务器的文件夹里的文件【/etc/yum.repos.d/】并且重命名为【 /etc/yum.repos.d/repo_bak/】
b1='''mkdir -p /etc/yum.repos.d/repo_bak/'''
b2='''mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/repo_bak/'''
# b3='''yum clean all'''
# 下载华为官方给出更换镜像源
b4='''wget http://mirrors.myhuaweicloud.com/repo/mirrors_source.sh && sh mirrors_source.sh'''
# 清除原有的yum缓存。
b5='''yum clean all'''
# 生成新yum缓存。
b6='''yum makecache'''







# 第二步
# 安装centos桌面图像
a2='''yum groupinstall "X Window System" -y'''
# 安装gnome
a3='''yum -y groups install "GNOME Desktop"'''
# 安装两个插件 【GNOME Desktop】 【Graphical Administration Tools】
# a4='''yum -y groups install "GNOME Desktop" "Graphical Administration Tools"'''
# 设置系统桌面环境默认启动
a5='''systemctl set-default graphical.target'''

# 执行命令
os.system(b1)
print("创建备份文件夹----已完成")
time.sleep(2)
os.system(b2)
print("已经移动到备份文件夹---已完成")
time.sleep(2)
os.system(b4)
print("下载华为云镜像文件---已完成")
time.sleep(2)
os.system(b5)
print("清处原有yum缓存--已完成")
time.sleep(2)
os.system(b6)
print("更新yum缓存--已完成")
time.sleep(2)

os.system(a2)
print("安装【X Window System】--已完成")
time.sleep(2)
# 安装一个插件----------------------------------
os.system(a3)
print("安装【GNOME Desktop】--已完成")
time.sleep(2)
# 安装一个插件----------------------------------
# 安装两个插件----------------------------------
# 如果要安装两个请 注释【安装一个插件】里的代码，把【安装两个插件】里的代码去掉注释
# os.system(a4)
# print("安装【GNOME Desktop】【Graphical Administration Tools】--已完成")
# time.sleep(2)
# 安装两个插件----------------------------------
os.system(a5)
print("已经设置默认启动桌面环境--已完成")
time.sleep(2)
print("请输出reboot 进行重启，再通过VNC方式登陆桌面")

# 上面的是执行安装图形化桌面