# -------------------------------------------------------------------------------
# Name:         GZ-WeiXinBot
# Purpose:      管理台登录相关.
#
# Author:       Liu.Qi
#
# Created:      20/10/2016
# Copyright:    (c) Chengdu Gerdige Technology Co., Ltd.
# -------------------------------------------------------------------------------

import cherrypy
import logging

from app.common import CommonTools
from app.common import Constants
from app.business.webapp import BotUser
from app.handler import WebHandler

from app.controller.RobotController import  Robot


class Login(object):

    __log = logging.getLogger()

    robot = Robot()

    @cherrypy.expose
    def index(self):
        if WebHandler.checkSession():
            return WebHandler.render_template(templatename="index.html", title='首页')
        # cherrypy.lib.sessions.expire()
        # print 'aaaa=' + cherrypy.request.__getattribute__().id
        # print 'dddd=' + cherrypy.session['_sessionid']
        #raise cherrypy.HTTPRedirect("/login")
        #raise cherrypy.HTTPRedirect("/login")

    @cherrypy.expose
    def login(self):
        return WebHandler.render_template(templatename="signin.html", title='登录')

    # 登录
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_in(on=True)
    @cherrypy.tools.json_out(on=True)
    @cherrypy.expose
    def loginIn(self):
        request = cherrypy.request.json
        wxnum = request['wxnum']
        pwd = CommonTools.md5(request['pwd'])

        self.__log.debug("[*] 账号[%s] 登录...", wxnum)

        flag = BotUser.queryUserByName(wxnum,pwd)

        self.__log.debug("[*] 账号[%s] 登录结果 %s", wxnum,flag)

        if flag :
            # 登录成功
            # 加载用户session
            cherrypy.session['_sessionid'] = cherrypy.session.id
            return {'stauts': True}
        else:
            return {'stauts': False}

    @cherrypy.expose
    def register(self):
        return WebHandler.render_template(templatename="signup.html", title='注册')

    # 注册
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_in(on=True)
    @cherrypy.tools.json_out(on=True)
    @cherrypy.expose
    def registerIn(self):
        request = cherrypy.request.json

        wxnum = request['wxnum']
        pwd = CommonTools.md5(request['pwd'])
        mobile = request['mobile']

        # 查询该用户是否存在
        flag = BotUser.queryUserByName(wxnum)

        if flag :
            return {'stauts': False,'msg':'用户已存在 ! '}
        else:
            flag = BotUser.regeiter(wxnum, pwd,mobile)
            if flag :
                # 注册成功
                return {'stauts': True}
            else:
                return {'stauts': False}