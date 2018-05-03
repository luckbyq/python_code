# -*- coding:utf-8 -*-
import requests,json

#微信公众号的ID和密钥，需要开通。
appid='<yourID>'
secret='<yourKEY>'

#获取access_token，并且赋值给data
def get_token():
    req=requests.post('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'% (appid,secret))
    data = json.loads(req.text)
    print data["access_token"]
    return data["access_token"]

# def get_template():
#     url = "https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token=" + get_token()
#
#     values = """{
#     "industry_id1":"1"
# }"""
#    print url

#使用url+token，再加上json的代码，实现发送模板。模板应该事先获得其全部字段。
def post_msg():
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + get_token()
    values = """{
    "touser": "<OpenID>",
    "template_id": "<templateID>",
    "data": {
        "o,one": {
            "value": "<text>",
            "color": "#173177"
        },
        "t,two": {
            "value": "<text>",
            "color": "#173177"
        },
        "e,end": {
            "value": "<text>",
            "color": "#173177"
        }
    }
}"""
    data = json.loads(values)
    req = requests.post(url, values)


post_msg()
# get_token()
# get_template()