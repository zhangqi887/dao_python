#!/bin/env python3

from app1 import app
from flask import jsonify,request
import json
import logging        #引入日志模块
logger = logging.getLogger(__name__)


@app.route('/hello')
def hello():
    """
        return hello
        hello
        /hello
        ---
        tags:
            - demo
        responses:
            200:
                description: Returns a json of itemgrp info
    """

    return jsonify({'msg':'hello'})
    
@app.route('/demo',methods=['POST'])
def demo():
    """
        demo service of json post
        demo
        curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"name":"goof"}' 'http://127.0.0.1:5000/demo'
        ---
        tags:
            - demo
        parameters:
            -   in: body
                name:  body
                description: demo
                required: true
                schema:
                    $ref: "#/definitions/Project"
        responses:
            200:
                description: Returns a json of worksheet exec log
        definitions:
          - schema:
                id: Project
                type: object
                properties:
                    name:
                        type: string
                required:
                    - name
    """
    logger.debug(request.data)
    params=json.loads(request.data)
    #params=json.loads(reques.data.decode("utf-8"))
    print(params)
    params=json.loads(request.data)
    return jsonify(params)