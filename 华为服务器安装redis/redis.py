# -*- coding: utf-8 -*-
# Python 2.X版本必须添加的开头

# centos7.2
# 本代码为脚本安装redis
# 请把本脚本文件放置到【/usr/local】目录里面
import os
# 导入系统操作库
import time
# 导入时间暂停库


# 第一步---------安装redis需要的tcl---------------------------------------------------------
# 安装redis【6.2.6】需要的tcl， centos7.2缺少tcl
os.system('''yum install tcl -y''')
# centos 7.2安装redis【6.2.6】的会报错
# 未执行第一步时，进入[/usr/local/redis/src]执行 [make test]
# 报错显示为：【You need tcl 8.5 or newer in order to run the Redis test】
# 安装tcl 
# yum install tcl -y
# 第一步---------安装redis需要的tcl---------------------------------------------------------

# 第二步----安装redis------------------------------------------------------------
# [https://redis.io/download]
# 下载6.2.6的redis
a1='''wget https://download.redis.io/releases/redis-6.2.6.tar.gz'''
a2='''tar -zxvf redis-6.2.6.tar.gz'''      # 解压【redis-6.2.6.tar.gz】包，得到【redis-6.2.6】文件夹
a3='''mv redis-6.2.6 /usr/local/redis'''   # 移动解压出来的【redis-6.2.6】文件夹至【/usr/local/目录下并且重命名为redis文件夹】
a4='''rm -f redis-6.2.6.tar.gz'''          # 删除下载的压缩包
a5='''cd /usr/local/redis && make'''       # 进入【/usr/local/redis】文件夹中,对解压出来的文件进行编译【make】 '''cd /usr/local/redis ; make'''

# 对编译完成后的文件进行安装【它将自动添加到环境目录中【/usr/local/bin】】
a6='''cd /usr/local/redis && make install'''#也可以执行 '''cd /usr/local/redis ; make install'''

# 好了它将自动添加到环境目录中【不需要自行创建软链接】

os.system(a1)
os.system(a2)
os.system(a3)
os.system(a4)
os.system(a5)
os.system(a6)

print("已经自动添加好了环境变量")
# 第二步----安装redis----------------------------------------------------------------



# 第二步 添加系统设置值-------------------------------------------------------------
# 设置   【在启动redis服务端时需要用到】


# 第二步 添加系统设置值--------------------------------------------------------------




# 第三步----设置redis的配置文件---------------------------------------------

# 原来安装redis里面会自动配备redis.conf文件,我喜欢统一存放在【/home/confs/】文件夹里面，所以有以下步骤

# 复制一个备份文件在原来的文件夹【 /usr/local/redis/redis_bak.conf】，备份文件名为【redis_bak.conf】
os.system('''mkdir -p /home/confs/''')#添加【-p】， 如果已经创建，则不提示
os.system('''cd /usr/local/redis && cp redis.conf redis_bak.conf''')# 复制并重命名
time.sleep(2)
print("拷贝成功redis_bak.conf")
# 移动【redis.conf】文件到【/home/confs】配置文件夹
os.system('''mv /usr/local/redis/redis.conf /home/confs''')
print("移动成功")
os.system('''cd /usr/local/redis && ls''')
print('''上面是【/usr/local/redis】里面的文件详情''')
time.sleep(10)
os.system('''cd /home/confs && ls''')
print('''上面是【/home/confs】里面的文件详情''')
time.sleep(10)

# 可选项A
# 如果你不想把服务配置文件放到【/home/conf/】文件夹里统一存放，请删除【/home/conf/reids.conf】文件。执行代码在下方：'
# 并且执行还原创建【 redis_bak.conf】文件的名字为【reids.conf】
# --------执行下面语句还原名字-------
# cd /usr/local/redis/ && mv redis_bak.conf redis.conf
#当你更改之后，启动命令为【redis-server /usr/local/redis/redis.conf】

# 第三步-------------------------------------------------------------------








# 第四步-------------设置允许分配物理内存-----------------------------------------------------

os.system('''sysctl vm.overcommit_memory=1''')
'''
设置
Linux的OOM机制在内存不足的情况下，会自动选择性杀死进程（点数过高的进程）
内核将检查是否有足够的可用内存供应用进程使用
0：不允许分配物理内存
1：允许分配所有的物理内存
2：允许分配超过所有物理内存和交换空间总和的内存
默认配置为：vm.overcommit_memory=0 
修改命令为：sysctl vm.overcommit_memory=1
'''

# 第四步-------------------------------------------------------------------






# 第五步----执行redis测试---------------------------------------------------------------
# 安装完成redis后提示执行redis测试【make test】，需要进入[/usr/local/redis/src]执行 [make test]
'''
这时将会显示：所有测试通过均无错误！清理：可能需要一些时间......好的
All tests passed without errors!
Cleanup: may take some time... OK
'''
# 执行测试
os.system('''cd /usr/local/redis/src && make test''')
# 第五步-------------------------------------------------------------------


# 打印提示
print("==="*30)
print("启动redis服务端:redis-server /home/confs/redis.conf")
print("启动redis客户端请在新建的会话框输入:redis-cli")
print("查看redis版本号:redis-cli -v")
print("关闭redis服务端:redis-cli shutdown")
time.sleep(5)
print("==="*30)