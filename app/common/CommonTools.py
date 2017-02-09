# coding: utf-8

import hashlib
import os
import re
import time
import uuid

from app.common import Constants


# 转MD5
# @param str 要转的字符串
# @param upper 默认True 转大写
def md5(str,upper=True):
    m5 = hashlib.md5(str.encode("utf8"))
    m5str = m5.hexdigest()
    if upper:
        return m5str.upper()
    return m5str

# 获取正则表达式的对象
def regxSearch(str,regx):
    return re.search(regx, str)

# 创建目录
# @param dirPath 文件夹路径 ，单级直接传名称， 从第一级之后用/分割
def makeDir(dirPath):
    dirName = os.path.join(Constants.APP_PATH, dirPath)
    if not os.path.exists(dirName):
        return os.makedirs(dirName)

# 返回当前时间字符串 YYYY-MM-DD HH24:mi:ss
def getCurrentTimeStr():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 保存文件
# @param dirPath 文件夹路径 ，单级直接传名称， 从第一级之后用/分割
# @param filename 文件名称
# @data 文件要写入的内容
def saveFile(dirPath , filename, data):
    fn = filename
    dirName = os.path.join(Constants.APP_PATH, dirPath)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    fn = os.path.join(dirName, filename)
    with open(fn, 'wb') as f:
        f.write(data)
        f.close()
    return fn

#
# 生成UUID
# @param key 默认空 按照UUID-1方式生成,
# 如果有值，者按照UUID-3规则生成。但是前提业务需保证key具有唯一性，如手机号
def getUUID(key=None):
    '''
        Python uuid 5种算法
        1、uuid1()——基于时间戳
               由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
               但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
        2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
                算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
                实际中很少用到该方法。
        3、uuid3()——基于名字的MD5散列值
                通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
                和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
        4、uuid4()——基于随机数
                由伪随机数得到，有一定的重复概率，该概率可以计算出来。
        5、uuid5()——基于名字的SHA-1散列值
                算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

        使用方面（官方建议）：

            首先，Python中没有基于DCE的，所以uuid2可以忽略；
            其次，uuid4存在概率性重复，由无映射性，最好不用；
            再次，若在Global的分布式计算环境下，最好用uuid1；
            最后，若有名字的唯一性要求，最好用uuid3或uuid5。
    '''
    if key is None:
        return str(uuid.uuid1()).upper()
    else:
        return str(uuid.uuid3(uuid.NAMESPACE_DNS,key)).upper()
