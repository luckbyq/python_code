#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2

url = '<sms api url>'

#格式化短信收件人为str，中间以逗号分隔。
smsuser = {
    '<name>' : '<phone>',
}

#工作，将需要发送的短信组成字符串。
tosms = ''
for key in smsuser:
    if len(tosms) > 1:
        tosms = tosms + ',' + smsuser[key]
    else:
        tosms = tosms + smsuser[key]

def postsms(content):
    post(content,tosms)


def post(content, tos):
    d = {
        'content': content,
        'tos': tos,
    }
    data = urllib.urlencode(d)
    req = urllib2.Request(url, data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req)
    return response.read()

if __name__ == "__main__":
    pass