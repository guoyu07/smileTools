#!/usr/bin/env python
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

import sqlite3
import logging

from app.common import Constants

'''
创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
创建在内存上面： conn = sqlite3.connect('"memory:')

下面我们一硬盘上面创建数据库文件为例来具体说明：
conn = sqlite3.connect('c:\\test\\test.db')
其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

    commit()            --事务提交
    rollback()          --事务回滚
    close()             --关闭一个数据库链接
    cursor()            --创建一个游标

cu = conn.cursor()
这样我们就创建了一个游标对象：cu
在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
对于游标对象cu，具有以下具体操作：

    execute()           --执行一条sql语句
    executemany()       --执行多条sql语句
    close()             --游标关闭
    fetchone()          --从结果中取出一条记录
    fetchmany()         --从结果中取出多条记录
    fetchall()          --从结果中取出所有记录
    scroll()            --游标滚动
'''

__log = logging.getLogger()

# 获取数据库连接
def __getConnection(retKV=False):

    conn = None

    try:

        conn = sqlite3.connect(Constants.DATABASE_PATH, timeout=10)

        if conn == None:
            __log.error("[*] can`t create database connect ! system will exit.")
            exit()

        '''
            Connection.text_factory使用此属性来控制我们可以从TEXT类型得到什么对象
            默认情况下，这个属性被设置为Unicode，sqlite3模块将会为TEXT返回Unicode对象。
            若你想返回bytestring对象，可以将它设置为str。
        '''
        conn.text_factory = str

        if retKV :
            '''
                官方文档规定，指定conn.row_factory ，在回调处理的函数中，处理row数据即可
            '''
            conn.row_factory = dict_factory

    except sqlite3.Error as e:
        __log.error("[*] can`t create database connect ! system will exit. \n %s " % (e))

    return conn


# 查询数据
# @param sql        sql语句，例:select name,age,sex from person where age > ? and sex = ?
# @param qvars      查询条件，例:[18,0]
# @return  返回键值对的数组
def query_RetKV(sql, qvars):
    conn = None
    cursor = None
    try:
        conn = __getConnection(True)
        cursor = conn.cursor()
        cursor.execute(sql, qvars)
        ret = cursor.fetchall()
        return ret

    except sqlite3.Error as e:
        __log.error("[*] Query sql exception. \n %s \n sql >>> %s \n qvars >>> %s" % (e, sql, qvars))
    finally:
        close(conn,cursor)
    return None

# 查询数据
# @param sql         sql语句，例:select name,age,sex from person where age > ? and sex = ?
# @param qvars       查询条件，例: [18,0]
# @return 数组返回，值的数组
def query_RetVA(sql,qvars):
    conn = None
    cursor = None
    try:
        conn = __getConnection()
        cursor = conn.cursor()
        cursor.execute(sql, qvars)
        ret = cursor.fetchall()
        return ret

    except sqlite3.Error as e:
        __log.error("[*] Query sql exception. \n %s \n sql >>> %s \n qvars >>> %s" % (e, sql, qvars))
    finally:
        close(conn,cursor)
    return None

# 插入数据
# @param sql         sql语句，例:insert into person values(?,?,?)
# @param dataArr     插入数据，例: [('aname',12,1),('bname',13,0)]
def insert(sql,dataArr):
    conn = None
    cursor = None
    try:
        conn = __getConnection()
        cursor = conn.cursor()
        for data in dataArr:
            cursor.execute(sql, data)
        conn.commit()
    except sqlite3.Error as e:
        #e.args[0]
        conn.rollback()
        __log.error("[*] Insert sql exception. \n %s \n sql >>> %s \n dataArr >>> %s" % (e, sql, dataArr))
    finally:
        close(conn,cursor)
    return None

# 执行查询
# update / delete
# @param sql         sql语句
# @param params      数据数组
#
# 例(update)：
# sql = update person set age = ? where name = ? and sex = ?
# params = [19,'张三',0]
#
# 例(delete)：
# sql = delete from person where age > ? and sex = ?
# params = [18,0]
def excute(sql,params):
    conn = None
    cursor = None
    try:
        conn = __getConnection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
    except sqlite3.Error as e:
        __log.error("[*] Excute sql exception. \n %s \n sql >>> %s \n qvars >>> %s" % (e, sql, params))
    finally:
        close(conn,cursor)
    return None

# 关闭
def close(conn,cursor):
    try:
        if cursor is not None:
            cursor.close()
    except sqlite3.Error as e:
        __log.error("[*] close connection cursor error. \n %s " % (e))
        cursor.close()

    try:
        if conn is not None:
            conn.close()
    except sqlite3.Error as e:
        __log.error("[*] close connection cursor error. \n %s " % (e))
        conn.close()

#
# 官方例子
#
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

