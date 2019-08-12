#!/bin/env python
# -*- coding: utf8 -*-
#通用app框架
#注，如果是标准的restful app,可考虑flask-restful-swagger-2/flask-restful-swagger
#for  python3
import logging        #引入日志模块
logger = logging.getLogger(__name__)
import gevent
from gevent.pywsgi import WSGIServer
from flask import Flask,redirect

from flask import abort,jsonify
from flask import make_response
from flask import url_for
from flask_swagger import swagger

#from DBUtils.PooledDB import PooledDB
#import cx_Oracle


#from gevent import monkey
#monkey.patch_all()   #整合telent才需要

app = Flask(__name__)
#app = Flask(__name__, static_folder='./static')
app.config.from_object('config')

#dsn=cx_Oracle.makedsn(app.config['ORACLE_HOST'],app.config['ORACLE_PORT'],app.config['ORACLE_SID'])
#pool = PooledDB(cx_Oracle,mincached=app.config['ORACLE_MINCACHED'],blocking=True,user=app.config['ORACLE_USER'],password=app.config['ORACLE_PASSWORD'],dsn=dsn)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/health', methods=['GET','POST'])
def health_handler():
    """
        Health check for Spring Cloud Sidecar
        First line is the summary: healthcheck  api
        All following lines until the hyphens is added to description
        ---
        tags:
          - health
        responses:
          200:
            description: Returns a json of status.normal is "up"
    """
    return jsonify({'status': 'up'})

@app.route('/test')
def test_handler():
    #str={'状态': '正常'}    #中文是可以的
    str1='''
print("in test")
def test():
    return 'hello"<[{中文}]>"'
t=test
'''
    str={'code':str1}
    return jsonify(str)
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)   	


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "WES API"
    return jsonify(swag)

@app.route('/apidocs')
def docs():
  return redirect('/static/index.html?url=/spec')

#引入外部的route/api ,导入的是整个模块文件.这样的模块是不能独立运行的
from app1.routes import hello,coldev,biz
# if app.config['DEBUG'] == True:
#     from app1.routes import mocksvr
    #from app1.mocksvr import *


#注册到服务中心

