#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author : admin
# @DATETIME : 2019/2/13 15:37
# @SOFTWARE : PyCharm

from wsgiref.simple_server import make_server
from hello import application

httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()