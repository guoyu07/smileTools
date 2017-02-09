# coding: utf-8
# -------------------------------------------------------------------------------
# Name:         GZ-WeiXinBot
# Purpose:      系统常量.
#
# Author:       Liu.Qi
#
# Created:      20/10/2016
# Copyright:    (c) Chengdu Gerdige Technology Co., Ltd.
# -------------------------------------------------------------------------------

import os

# ---------------------------------------------------
# 系统常量
# ---------------------------------------------------

# 部署路径
APP_PATH = os.getcwd()  #os.path.abspath(os.getcwd())

# webapp路径
WEBAPP_PATH = os.path.join(APP_PATH,'webapp/')

# 运行时临时文件存放
APP_RUNTIME_PATH = os.path.join(APP_PATH,'runtime/')

# 日志路径
LOG_FILE_DIR_PATH = os.path.join(APP_PATH, 'log')

# 日志文件名
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR_PATH, 'app.log')

# 配置文件路径
CONFIG_FILE_PATH = os.path.join(APP_PATH, 'config/')

# ---------------------------------------------------
# 快递查询-快递鸟
# ---------------------------------------------------
# 快递鸟 商铺ID
KUAIDINIAO_APP_ID = "修改为您的快递鸟商铺号"

# 快递鸟 APP_KEY
KUAIDINIAO_APP_KEY = "修改为您的快递鸟APP_KEY"

# 单号识别 type
KUAIDINIAO_JISHI_REQUEST_TYPE = '1002'

# 单号识别 type
KUAIDINIAO_DANHAO_REQUEST_TYPE = '2002'

# 物流跟踪 type
KUAIDINIAO_GENZONG_REQUEST_TYPE = '1008'