#!/usr/bin/env python
#coding=utf-8
from urllib import parse
from urllib import request
import json, ssl          
def sendGM(sender,receiver,body):
    url = "https://im.sdo.com:9091/plugins/sndaalarm/send.do"
    data = {"sender":sender,"receiver":receiver,"body":body}
    param = parse.urlencode(data).encode(encoding='UTF8')
    f = request.urlopen(url, param)
    result = json.load(f)
    return result
 
if __name__ == '__main__': 
    sender = "alert"
    receiver = ['sndaliuhongyi']
    body = "这是我们的测试"
    kk = sendGM(sender,receiver,body)
    if kk['message'] == "success" and kk['status'] == "1":
        print("message send OK")
    else:
        print("message send error")

