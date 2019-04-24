#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : admin
# @DATETIME : 2019/2/13 15:35
# @SOFTWARE : PyCharm

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body = '<h3>Hello,%s!</h3>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]
