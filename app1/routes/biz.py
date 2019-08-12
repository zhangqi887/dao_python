#!/bin/env python3

from app1 import app
from DbPoolUtil import pool_util_oracle
#from app1 import pool
from flask import jsonify,request
import json

import logging
logger = logging.getLogger(__name__)

@app.route('/biz/api/v1/biz/wes/uptsubtaskinfo',methods=['POST'])
def uptsubtaskinfo_handle():
    """
        a rest service for update subtaskinfo
        biz
        /biz/api/v1/biz/wes/uptsubtaskinfo
        ---
        tags:
            - biz
        definitions:
          - schema:
              id: Task
              properties:
                wsid:
                  type: string
                  description: 工单id
                devid:
                  type: string
                  description: 设备id
                role:
                  type:  string
                  description: 角色
                cfgitemcode:
                  type:  string
                  description: 配置项编码
        parameters:
            -   in: body
                name:  body
                description: 子任务信息
                required: true
                schema:
                  type: object 
                  properties:
                    taskinfo:
                      type: array
                      description: list of subtaskinfo
                      items:
                        $ref: "#/definitions/Task"
                  required:
                      - taskinfo
        responses:
            200:
                description: Returns a json of resultinfo
                
    """
    logger.debug(request.data)
    params=json.loads(request.data)
    #params=json.loads(reques.data.decode("utf-8"))
    #print(params)
    #logger.debug(params["wsid"])
    return jsonify({'code':'biz-uptsubtaskinfo-0000','data':[]})
