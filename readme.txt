欢迎使用文件监视器 TheMachinev1.1

##使用方法##
修改文件目录下的 config.ini 配置文件，参考后文。
双击 run.py即可。

##原理介绍##
使用散列函数，获取文件的 MD5 值后保存，每隔一段时间（timer）重新生成文件新 MD5 值，对比新旧 MD5 值。如不一致，则通知邮件。
预先保存一份。调用pandas的compare方法获取具体的变化单元格

##配置文件参数介绍##
注！测试版本，请严格按照提示修改，否者易引起报错
[config]
#需要监控的文件的绝对路径，注意斜杠反斜杠。
filelocation = C:/Users/18436/Desktop/new 1.txt
#设置轮询时间 单位秒
timer = 5

[mailConfig]
#邮件服务器登录名及发件人地址
fromAddr = xxxxzz@163.com

#邮件服务器密码，密码为163邮箱授权密码，不是密码，方法（qq邮箱类似）：登录到163邮箱>>设置>POP3/SMTP/IMAP 中开启SMTP
password = NxxxxxxxP

#需要通知的邮箱
toAddr = xxxxx@qq.com

#邮件服务器地址
smtpServer = smtp.163.com
#发件人名称
formAlias = The Machine
#收件人名称
toAlias = 尊敬的马哥儿
#通知邮件主题
subjict = 来自The Machine的文件变化通知
#通知邮件内容
info = 马哥儿，马哥儿，你关注的文件发生变化了，快来看看呀!

##即将更新的功能##
v1，检测文件是否发生变化，发送邮件提醒
v2，检测具体那一行数据变了。
可检测excel具体某单元格发生变化，可发送附件，可抄送，生成历史记录
v3，图形化界面
v4，能检测网页
