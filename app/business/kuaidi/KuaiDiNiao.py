# -------------------------------------------------------------------------------
# Purpose:      快递鸟即时查询.
#
# Author:       Liu.Qi
#
# Created:      09/02/2017
# Copyright:    (c) Chengdu Gerdige Technology Co., Ltd.
# -------------------------------------------------------------------------------

import json
from app.handler import KuaiDiQueryHandler
from app.common import Constants


#
# 即时查询
# ShipperCode 物流公司编码
# LogisticCode 物流单号
# return json物流数据
# 例如
# {
# 'EBusinessID': 'xxx',
# 'ShipperCode': 'STO',
# 'Success': True,
# 'LogisticCode': 'xxxx',
# 'State': '3',
# 'Traces': [
#   {'AcceptTime': '2017-02-05 17:50:09', 'AcceptStation': '【收件】【陕西西安公司】的【xxx】已收件,扫描员是【xxx】'},
#   {'AcceptTime': '2017-02-06 13:55:12', 'AcceptStation': '【收件】【陕西西安公司】的【xxx】已收件,扫描员是【xxx】'},
#   {'AcceptTime': '2017-02-06 20:43:36', 'AcceptStation': '【到件】快件到达【陕西西安航空部】,上一站是【陕西西安公司】,扫描员是【xxxx】'},
#   {'AcceptTime': '2017-02-06 21:04:32', 'AcceptStation': '【装袋】【陕西西安航空部】已进行【装袋】扫描,袋号【xxxx】单号【xxxx】'},
#   {'AcceptTime': '2017-02-06 21:04:32', 'AcceptStation': '【发件】快件在【陕西西安航空部】由【腊家扫描员叁叁】扫描发往【xxxx】'},
#   {'AcceptTime': '2017-02-07 01:44:00', 'AcceptStation': '【发件】快件在【陕西西安航空部】由【腊家扫描员柒号】扫描发往【xxxx】'},
#   {'AcceptTime': '2017-02-07 19:26:42', 'AcceptStation': '【发件】快件在【xxxx】由【xxx】扫描发往【xxxx】'},
#   {'AcceptTime': '2017-02-08 07:18:14', 'AcceptStation': '【到件】快件到达【xxxx】,上一站是【】,扫描员是【xxx】'},
#   {'AcceptTime': '2017-02-08 08:03:57', 'AcceptStation': '【派件】【xxx】的【xxx】正在派件,扫描员是【xxx】'},
#   {'AcceptTime': '2017-02-08 10:29:11', 'AcceptStation': '【签收】已签收,签收人是:【xxxxx单元申通】'}
# ]}
#
def realtimeQuery(ShipperCode,LogisticCode):
    requestData = {
        "OrderCode": "",  # 订单号
        "ShipperCode": ShipperCode,
        "LogisticCode": LogisticCode
    }
    data = json.dumps(requestData, sort_keys=True)
    post_data = {
        'RequestData': data,
        'EBusinessID': Constants.KUAIDINIAO_APP_ID,
        'RequestType': Constants.KUAIDINIAO_JISHI_REQUEST_TYPE,
        'DataType': '2',
        'DataSign': KuaiDiQueryHandler.getDataSign(data)
    }

    return KuaiDiQueryHandler.realtimeQuery(post_data)

#
# 即时查询
# LogisticCode 物流单号
# 返回该单号快递公司编码及名称
# 例如：{'EBusinessID': 'xxx', 'Success': True, 'LogisticCode': 'xxxx', 'Shippers': [{'ShipperCode': 'STO', 'ShipperName': '申通快递'}]}
#
def billnoQuery(LogisticCode):
    requestData = {
        "LogisticCode": LogisticCode
    }
    data = json.dumps(requestData, sort_keys=True)
    post_data = {
        'RequestData': data,
        'EBusinessID': Constants.KUAIDINIAO_APP_ID,
        'RequestType': Constants.KUAIDINIAO_DANHAO_REQUEST_TYPE,
        'DataType': '2',
        'DataSign': KuaiDiQueryHandler.getDataSign(data)
    }

    return KuaiDiQueryHandler.billnoQuery(post_data)

# 物流跟踪
def genzongQuery():
    return



