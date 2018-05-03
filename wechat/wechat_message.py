# -*- coding:utf-8 -*-
import requests,json,sys

#获取执行python的第二个参数之后的所有参数等于msg（第一个参数为脚本本身）。
msg=sys.argv[1:]

#微信公众号获得的用户的openID，需要通知多少人，就往里加。
user=['OPENID','OPENID']

#微信公众号的ID和密钥，需要开通。
appid='<yourID>'
secret='<yourKEY>'

#获取access_token，并且赋值给data
def get_token():
    req=requests.post('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&%s&%s'% (appid,secret))
    data = json.loads(req.text)
    return data["access_token"]


#使用json格式，发送消息给用户
def send_msg(name,masage):
    url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=" + get_token()

    values = """{
    "touser": "%s",
    "msgtype": "text",
    "text": {
        "content": "%s"
    }
}""" % (name,masage)

    data = json.loads(values)
    req = requests.post(url, values)

#循环将所有的用户都通知到。
if __name__ == '__main__':
    for i in user:
        send_msg(i,msg)
