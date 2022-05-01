import configparser
import hashlib
import os
import smtplib
import time
import configparser
from email import encoders, header
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr
import os
import smtplib

import time

# 获取文件的md5


def getFileMD5(fileLocation):

    file = open(fileLocation, "r",encoding="utf-8")
    filestring = file.read()
    file.close()
    m = hashlib.md5(filestring.encode(encoding='utf-8')).hexdigest()
    return(m)

# 对比新旧文件


def checkIt(location):
    newMD5 = getFileMD5(location)
    if not os.path.exists('./record.txt'):
        f = open('./record.txt', "w",encoding="gbk")
        f.write(newMD5)
        f.close()
    file1 = open("./record.txt", "r")
    oldMD5 = file1.read()
    file1.close
    # print("new："+newMD5)
    # print("old: "+oldMD5)
    if newMD5 != oldMD5:
        file = open("./record.txt", "w")
        file.write(newMD5)
        file.close()
        return(True)
    else:
        return(False)

# 计时器


def setTimer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("计时器", timer, end="\r")
        time.sleep(1)
        t -= 1

# 用于格式化邮件地址


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 用于发送邮件


def sendIt():
    # 从config中获取邮件配置信息
    cf = configparser.ConfigParser()
    cf.read(".\config.ini", encoding="utf-8")
    # 基本信息，其中密码为163邮箱授权密码，方法：登录到163邮箱>>设置>>POP3/SMTP/IMAP 中开启SMTP
    fromAddr = cf.get('mailConfig', 'fromAddr')
    password = cf.get('mailConfig', 'password')
    toAddr = cf.get('mailConfig', 'toAddr')
    smtpServer = cf.get('mailConfig', 'smtpServer')

    # 构建邮件
    msg = MIMEText(cf.get('mailConfig', 'info'), 'plain', 'utf-8')
    msg['From'] = _format_addr('%s <%s>' % (
        cf.get('mailConfig', 'formAlias'), fromAddr))
    msg['To'] = _format_addr('%s <%s>' % (
        cf.get('mailConfig', 'formAlias'), toAddr))
    msg['Subject'] = Header(cf.get('mailConfig', 'info'), 'utf-8').encode()

    # 发送出去
    sendMail = smtplib.SMTP(smtpServer, 25)
    sendMail.set_debuglevel(1)
    sendMail.login(fromAddr, password)
    sendMail.sendmail(fromAddr, toAddr, msg.as_string())
    sendMail.quit()


def getTime():
    tick = int(time.time())
    timeArray = time.localtime(tick)
    normalTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return normalTime


# 程序主体
config = configparser.ConfigParser()
config.read(".\config.ini", encoding="utf-8")
print("[%s] 开始监测文件 %s" % (getTime(), config.get("config", "fileLocation")))
while True:
    flag = checkIt(config.get("config", "fileLocation"))
    if flag:
        print("[%s] 已变，准备发送邮件" % getTime())
        sendIt()
        print("[%s] 邮件已发送" % getTime())
    else:
        print("[%s] 无变化" % getTime())
    setTimer(int(config.get("config", "timer")))
