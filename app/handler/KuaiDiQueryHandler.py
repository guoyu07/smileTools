# -------------------------------------------------------------------------------
# Purpose:      快递查询相关配置.
#
# Author:       Liu.Qi
#
# Created:      09/02/2017
# Copyright:    (c) Chengdu Gerdige Technology Co., Ltd.
# -------------------------------------------------------------------------------

import json
import urllib
import urllib.request
import hashlib
import base64
import urllib.parse
import logging
import time

from app.common import Constants

__log = logging.getLogger()

#
# 快递鸟 签名数据
# 数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码
#
def getDataSign(request_Data):
    """数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码"""
    m = hashlib.md5()
    m.update((request_Data + Constants.KUAIDINIAO_APP_KEY).encode("utf8"))
    encodestr = m.hexdigest()
    base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))

    __log.debug("快递鸟-快递查询-获取加密签名，%s",base64_text.decode())

    return base64_text.decode()

#
# 执行post提交
#
def sendpost(url,datas):
    """发送post请求"""
    postdata = urllib.parse.urlencode(datas).encode('utf-8')
    header = {
        "Accept": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "utf-8"
    }

    try:

        beginTime = time.clock()

        req = urllib.request.Request(url, postdata, header)
        get_data = (urllib.request.urlopen(req).read().decode('utf-8'))

        endTime = time.clock()

        __log.debug("快递鸟-快递查询-发送POST，url[%s],请求参数[%s] ", url,postdata)
        __log.debug("快递鸟-快递查询-发送POST，Header[%s] ", header)
        __log.debug("快递鸟-快递查询-发送POST，耗时[%f],返回值[%s] ", (endTime - beginTime),get_data)

        return get_data
    except Exception as e:
        __log.error("[*] 执行Post请求出错 .. %s" , e)
        print (Exception, ":", e)


# 即时查询
def realtimeQuery(post_data):
    url = 'http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx'
    json_data = sendpost(url, post_data)
    return json.loads(json_data)

# 单号查询
def billnoQuery(post_data):
    url = 'http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx'
    json_data = sendpost(url, post_data)
    return json.loads(json_data)

# 物流跟踪
def genzongQuery(post_data):
    url = 'http://api.kdniao.cc/api/dist'
    json_data = sendpost(url, post_data)
    return json.loads(json_data)
