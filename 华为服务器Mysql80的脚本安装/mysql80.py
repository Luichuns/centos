# -*- coding: utf-8 -*-
# python2.7.5版本支持的ASCII码是无中文的，开头的必须添加

#请把本文件复制至home目录下，并在home目录中执行：cd /home


#centos7.4/7.2的自带python版本是2.7.5 查看命令为python -V
import os#导入系统基本操作库
import time#导入时间库

##第一步 【停止mysql服务】
a1="service mysqld stop"
os.system(a1)
time.sleep(5)#休眠5秒等待执行

# 第二步【卸载mariadb】
#停止mariadb
a2="service mariadb stop"
os.system(a2)
time.sleep(5)#休眠5秒等待执行
#卸载
a3="yum remove mariadb mariadb-server"
#如果你还未进入超级管理员方式，请进入超级管理员方式执行：【sudo yum remove mariadb mariadb-server】
os.system(a3)

##第三步 删除mysql文件夹，然后删除
"""
系统里面的路径为mysql: /usr/lib64/mysql /usr/share/mysql
"""
a4="whereis mysql"#验证查找mysql服务
os.system(a4)
time.sleep(5)#休眠5秒等待执行


#下面的目的是为了执行删除mysql
"""
rm -rf /usr/lib64/mysql
rm -rf /usr/share/mysql
"""

a5="rm -rf /usr/lib64/mysql"#删除目录
a6="rm -rf /usr/share/mysql"#删除目录
os.system(a5)
time.sleep(2)#休眠2秒
os.system(a6)
time.sleep(2)#休眠2秒


#第四步 删除mysql软件相关的包
b1="rpm -qa|grep -i mysql"#找到所有mysql相关的包
os.system(b1)
"""
centos7.4并没有显示相关的包,所以下面的注释可以不执行,不是centos7.4，需要查看下"""



#第五步【删除mysql相关的 mariadb包】
"""
找到所有mysql相关的包 mariadb包
目的是执行删除命令
sudo rpm -ev --nodeps mariadb-libs-5.5.56-2.el7.x86_64
mariadb-libs-5.5.56-2.el7.x86_64
mariadb-libs-5.5.68-1.el7.x86_64 （centos7.4 8核16g的显示的是这个安装包）"""

c1="rpm -qa|grep mariadb"#查看mariadb的安装包是否存在，存在则删除
os.system(c1)
c2="rpm -ev --nodeps mariadb-libs-5.5.68-1.el7.x86_64"#删除包命令字符
os.system(c2)
#非超管请执行：【sudo rpm -ev --nodeps mariadb-libs-5.5.56-2.el7.x86_64】
print("""下面显示为查看mariadb安装包是否存在，不存在请等10秒，否则请停止执行【ctrl+c】""")
os.system(c1)#再次执行，查看mariadb安装包是否存在
time.sleep(10)
print("")


#第六步 【删除mysql的配置信息】
'''
k="rm /etc/my.cnf"# centos7.4里面并没有这个配置，可以不执行，如果是其他版本需要查看下
os.system(k)# 删除mysql配置信息
'''

#第七步【下载mysql8.0【安装器】的安装包，并进行安装】

#下载
d1="wget https://dev.mysql.com/get/mysql80-community-release-el7-4.noarch.rpm"#下载centos7.4版本
os.system(d1)

"""
centos7.4里面是有wget的，不需要安装
如需要安装wget，请执行【yum install wget】
"""
"""
其它版本
https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
https://dev.mysql.com/get/mysql80-community-release-el7-4.noarch.rpm
"""

#显示
print("已经下载好了mysql8.0的安装包的连接文件")
os.system("""ls""")
time.sleep(5)#休眠5秒等待执行

#安装
d2="rpm -ivh mysql80-community-release-el7-4.noarch.rpm"
os.system(d2)
"""
非超级管理员请使用：sudo rpm -ivh mysql80-community-release-el7-4.noarch.rpm
"""

print("""添加好了mysql8.0的包连接文件到本地的yum库中""")
time.sleep(10)#休眠5秒等待执行


# 第八步【更新缓存，让新的缓存生效】
#更新缓存
print("""将服务器上的软件包信息,进行本地缓存,以提高搜索或安装软件的速度，更新下载包的信息""")
d3="yum makecache"
os.system(d3)

# 显示信息
print("""更新缓存完毕""")
time.sleep(3)#休眠3秒

# 第九步【执行安装mysqlserver】
print("""进行安装匹配的mysql服务端，这个过程需要5分钟""")
d4="yum install mysql-community-server -y"
os.system(d4)
"""非超级管理员请用：sudo yum install mysql-community-server -y"""




# 第十步【显示安装mysql后的状态，是否在运行】
d5="service mysqld status"
os.system(d5)
print("""mysql已经安装在：/usr/lib/systemd/system/mysqld.service
准备启动mysql服务
""")
time.sleep(5)
"""
显示为Active:active(running) 表示在运行
显示为Active:inactive(dead) 表示在被杀死了，停止
"""

# 第十一步【启动mysql】
#启动
d6="service mysqld start"
os.system(d6)
#显示提醒信息
print("""已经启动mysql服务""")
time.sleep(20)


# 第十二步【使用自动生成的密码进入mysql】
"""
查看自动生成的密码
sudo grep 'temporary password' /var/log/mysqld.log
"""
#获取密码
d7="sudo grep 'temporary password' /var/log/mysqld.log"
d8=os.popen(d7)#获取执行terminal命令后得到的对象
d9=str(d8.readlines())#读取对象的列表，并且转化为字符串
d10=d9.split()#使用空格符号切片
d11=d10[-1]# 获取到的字段末尾还是有【\n】
d12=d11[0:12]#通过字符串的切割方式获取  密码【一般为12位字符】
d13="mysql -uroot -p"#命令拼接
d14=d13+'"'+d12+'"'
print("""mysql8.0会自动生成初次密码【12位数的密码】""")
print("""登录时请使用该密码""")

# 执行进入mysql
os.system(d14)



# 第十三步【进入修改密码和更改验证方式 】
#【说明】：修改密码的验证方式 
'''
在 MySQL 8.0 中，默认身份验证插件已由 
【旧的】mysql_native_password 更改为 
【新的】caching_sha2_password，


如果你想要使用旧的身份验证插件，可以：
【使用ALTER USER如下修改账号认证插件和新密码：】
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
-----------------------------------
下次登录请不要使用【mysql -uroot -p"EOqRmvspO7/Y"】这种明文密码
请使用【mysql -uroot -p】+【回车】
进入密文模式输入密码

'''

# 【执行】进入mysql之后，设置验证方式和更改新的密码
print("""请复制下面的命令去修改你的【新密码】
密码格式要求:【大写字符】【小写字母】+【数字】+【符号】
alter user 'root'@'localhost' identified with mysql_native_password by '新密码';
请复制上面这行
修改完密码后退出输入【exit;】
------------------------------------------------------------------
下次登录请不要使用【mysql -uroot -p"EOqRmvspO7/Y"】这种明文密码
请使用【mysql -uroot -p】+【回车】
进入密文模式输入密码：【新密码】
""")

d15="use mysql;"
os.system(d15)






#第十五步【可选】：更换新的加密验证方式
"""
如果你要更改会新的验证插件方式强进入mysql后执行
alter user 'root'@'localhost' identified with caching_sha2_password by '密码';
"""

