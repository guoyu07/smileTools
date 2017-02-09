# coding: utf-8
# -------------------------------------------------------------------------------
# Name:         GZ-WeiXinBot
# Purpose:      发起Get、Post请求，参数处理.
#
# Author:       Liu.Qi
#
# Created:      20/10/2016
# Copyright:    (c) Chengdu Gerdige Technology Co., Ltd.
# -------------------------------------------------------------------------------

import urllib.request
import urllib.parse
import json
import logging


__log = logging.getLogger()

# 执行Get 请求
def _GET(url, api=None, times=3):
    request = urllib.request.Request(url)
    request.add_header('Referer', 'https://wx.qq.com/')
    if api == 'webwxgetvoice':
        request.add_header('Range', 'bytes=0-')
    if api == 'webwxgetvideo':
        request.add_header('Range', 'bytes=0-')

    data = None

    try:
        response = urllib.request.urlopen(request)
        data = response.read()
        # logging.debug(url)
        return data
    except Exception as e:
        __log.error("[*] 执行Get请求出错 .. %s",url)
        print(Exception, ":", e)
        #重试
        if times > 0 :
            data = _GET(url,api,times-1)

    return data

# 执行post请求
def _POST(url, params, jsonfmt=True):
    if jsonfmt:
        request = urllib.request.Request(url=url, data=json.dumps(params))
        request.add_header('ContentType', 'application/json; charset=UTF-8')
    else:
        request = urllib.request.Request(url=url, data=urllib.parse.urlencode(params))

    data = None

    try:
        response = urllib.request.urlopen(request)
        data = response.read()
        if jsonfmt:
            return json.loads(data, object_hook=_decode_dict)
    except Exception as e:
        __log.error("[*] 执行Post请求出错 .. ")
        print (Exception, ":", e)

    return data

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, str):#isinstance(key, unicode)
            key = key.encode('utf-8')
        if isinstance(value, str):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, str):##isinstance(item, unicode)
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv