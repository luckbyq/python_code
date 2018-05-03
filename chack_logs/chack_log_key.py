#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess,mail,sms,commands,sys

#测试是否获取到传入参数，如果未获取到则提示并退出
try:
    logfile = sys.argv[1]
except:
    print "the commands is   \"nohup python chack_log_key.py <log dir> >/dev/null 2>&1 &\" "
    exit(1)

#赋值 项目名称，本机IP，本机hostname
proname = ' '.join(logfile.split("/")[-3:-1])
ip = commands.getoutput("/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|grep 10.|tr -d \"addr:\"")
hostname = commands.getoutput("/bin/hostname")

#工作模块。查看指定的日志文件中是否有指定的关键字。
def chack_log(logfile):
    command='tail -f 200 %s' % logfile
    popen=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    while True:
        line=popen.stdout.readline().strip()
        #关键字如果存在，则报警。
        if ("acquisition failure" in line) or (" sync update" in line) or ("[ERROR]" in line):
            mail.mail(subject="Project : %s     is problem" % proname,

                      message="Hostname : %s\n\nIP address : %s\n\nThe Log have acquisition failure or sync update or [ERROR],please chack it\n\nThe error line is %s\n\n" % (hostname, ip, line),
                      enclosure="none")
            sms.postsms("Project : %s     is problem" % proname)


chack_log(logfile)