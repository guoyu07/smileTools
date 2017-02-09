# coding: utf-8
# -------------------------------------------------------------------------------
# Name:         GZ-WeiXinBot
# Purpose:      日志文件配置.
#
# Author:       Liu.Qi
#
# Created:      20/10/2016
# Copyright:    (c) Chengdu Gerdige Technology Co., Ltd.
# -------------------------------------------------------------------------------

import logging
import logging.config
#import coloredlogs

from app.common import Constants
from app.common import CommonTools

logInit = False

# 初始化日志
def __init():
    __checkLogDir()
    __loadConfig()
    __loadColorLog()
    logInit = True

# 检查日志路径
def __checkLogDir():
    CommonTools.makeDir(Constants.LOG_FILE_DIR_PATH)

# 加载日志配置文件
def __loadConfig():
    logging.config.fileConfig(Constants.CONFIG_FILE_PATH + 'logger.conf')

# 加载日志颜色模块
def __loadColorLog():

    # coloredlogs
    #
    # https://coloredlogs.readthedocs.io/en/latest/
    #
    # coloredlogs.install(level=None, **kw)
    #
    # level – The default logging level (an integer or a string with a level name, defaults to logging.INFO).
    # logger – The logger to which the stream handler should be attached (a Logger object, defaults to the root logger).
    # fmt – Set the logging format (a string like those accepted by Formatter, defaults to DEFAULT_LOG_FORMAT).
    # datefmt – Set the date/time format (a string, defaults to DEFAULT_DATE_FORMAT).
    # level_styles – A dictionary with custom level styles (defaults to DEFAULT_LEVEL_STYLES).
    # field_styles – A dictionary with custom field styles (defaults to DEFAULT_FIELD_STYLES).
    # stream – The stream where log messages should be written to (a file-like object, defaults to sys.stderr).
    # isatty – True to use a ColoredFormatter, False to use a normal Formatter (defaults to auto-detection using terminal_supports_colors()).
    # reconfigure – If True (the default) multiple calls to coloredlogs.install() will each override the previous configuration.
    # use_chroot – Refer to HostNameFilter.
    # programname – Refer to ProgramNameFilter.
    # syslog – If True then enable_system_logging() will be called without arguments (defaults to False).

    #coloredlogs.install(fmt='[%(asctime)s] [%(filename)s] [line:%(lineno)d] [%(name)s][%(levelname)s] %(message)s',reconfigure=True)

    return

# 获取日志对象
def getLogger(modelueName=''):
    if logInit == False:
        __init()
    return logging.getLogger(modelueName)