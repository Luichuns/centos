# -*- coding: utf-8 -*-
# Python 2.X版本必须添加的开头

# luichun

# centos7.0 版本下载 mongodb5.0.5版本
# 下载mongodb的链接
# https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-5.0.5.tgz

# 本文件复制至centos的home文件目录文件夹中

# 第一步
# 把本代码复制至/home/文件夹中
# cd进入到/home/文件夹中
# cd /home
# 执行 python mongojiaoben.py

import os
import time



# 第二步
# 创建文件夹
a1='''mkdir -p /usr/local/mongodb'''
# 下载mongodb文件包
a2='''wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-5.0.5.tgz'''
# 在当前文件夹中解压
a3='''tar -xvf ./mongodb-linux-x86_64-rhel70-5.0.5.tgz'''
# 得到的文件夹为【mongodb-linux-x86_64-rhel70-5.0.5】
# 【把解压出来的文件夹里面的文件】都移动到【新的文件夹中】  [mongo文件夹中]  并且重命名为mongodb
a4='''mv mongodb-linux-x86_64-rhel70-5.0.5/* /usr/local/mongodb'''
# 建立软连接
# mongod为服务端
# mongo为客户端
a5='''ln -s /usr/local/mongodb/bin/mongod /usr/local/bin/mongod'''
a6='''ln -s /usr/local/mongodb/bin/mongo /usr/local/bin/mongo'''


os.system(a1)
print("已经创建好mongodb文件夹--【/usr/local/mongodb】")
os.system(a2)
print("已经下载好了mongodb文件包---完成")
time.sleep(2)
os.system(a3)
print("已经解压好了mongodb文件包---完成")
time.sleep(2)
os.system(a4)
print("已经移动到/usr/local/mongo/文件夹里面---完成")
time.sleep(2)
os.system(a5)
os.system(a6)
print("已经创建好mongod服务端，mongo客户端的软连接到环境目录---完成")
time.sleep(2)



# 第三步
# 创建配置文件需要的文件夹
b1='''mkdir -p /home/mongo/.mongodb/data/'''
os.system(b1)
print("已经在本目录下创建了mongod-27017.conf配置文件文件")
time.sleep(2)
# 创建一个专门用于配置的confs文件夹
b2='''mkdir -p /home/confs/'''
# 创建mongodb的配置文件夹
os.system(b2)
print("已经在创建好【/home/confs/】文件夹")
time.sleep(2)


# 第四步创建并写入配置文件【mongod-27017.conf】
c1='''#绑定ip
bind_ip=0.0.0.0
# 存放数据的文件夹位置在
dbpath=/home/mongo/.mongodb/data/
#向外暴露的端口为
port=27017
#日志文件位置
logpath=/home/mongo/.mongodb-27017.log
#启动追加模式添加数据（false则为没启动一次则重新创建一个日志文件）
logappend=true
#开启后台运行，否则关闭启动窗口则即刻停止服务端
fork=true
'''

# 创建一个文件[mongod-27017.conf],写入时必须为utf-8格式,因为python2写入的是二进制
fo=open("mongod-27017.conf","w")
#写入数据文件
fo.write(c1)
# 保存关闭文件
fo.close()

print("已经在本目录下创建了mongod-27017.conf配置文件文件")

# 第五步：移动创建好的配置文件到/home/conf/的配置文件夹中
d1='''mv mongod-27017.conf /home/confs/'''
os.system(d1)
print("已经把配置文件移动到【/home/confs/】的配置文件夹中")
time.sleep(2)


print("启动mongod服务端")
d2='''mongod -f /home/confs/mongod-27017.conf'''
time.sleep(2)
os.system(d2)
print("请执行以下代码启动客户端")
print("mongo --host 127.0.0.1 -port 27017")
print("如需要开机启动，请自行配置")


