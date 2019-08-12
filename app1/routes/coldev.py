#!/bin/env python3

from app1 import app
from DbPoolUtil import pool_util_oracle
#from app1 import pool
from flask import jsonify,request
import json

import logging
logger = logging.getLogger(__name__)

@app.route('/cold/api/v1/res/dev/getdevcolinfo/<string:deviceid>',methods=['GET'])
def getdevinfo(deviceid):
    """
        data of Get Device Info by deviceid
        dev
        /cold/api/v1/res/dev/getdevcolinfo/{devceid}
        ---
        tags:
            - dev
        parameters:
            -   in: path
                name: deviceid
                description: 设备标识
                required: true
                type: string
                format: string
        responses:
            200:
                description: Returns a json of device info
    """

    print(deviceid)
    DString = 'beijingtiananmen'
    # conn = pool.connection()
    # cur = conn.cursor()

    # # SQL = "SELECT D1.DEVICEID,D1.DEVICENAME,D1.LOOPADDRESS,D1.PROMPT,D1.LOGINTYPE,D1.USERNAME,\
    # #                         decode(D1.PASSWORD,null,D1.PASSWORD,decrypt_data(D1.PASSWORD,?)) AS PASSWORD,\
    # #                         decode(D1.ENABLEPASSWD,null,D1.ENABLEPASSWD,decrypt_data(D1.ENABLEPASSWD,?)) AS ENABLEPASSWD,\
    # #                         decode(D1.ROCOMMUNITY,null,D1.ROCOMMUNITY,decrypt_data(D1.ROCOMMUNITY,?)) AS ROCOMMUNITY,\
    # #                         D1.RWCOMMUNITY,\
    # #                         D1.ISNEW,D1.DEVICETYPECODE,D1.DEVICEMODELCODE,D1.NODECODE,D1.DETAILMODELCODE,\
    # #                         D1.SNMPVERSION,D1.SNMPUSERNAME,D1.SNMPAUTHPROTOCOL,\
    # #                         decode(D1.SNMPAUTHPASSWORD,null,D1.SNMPAUTHPASSWORD,decrypt_data(D1.SNMPAUTHPASSWORD,?)) AS SNMPAUTHPASSWORD,\
    # #                         D1.SNMPPRIVPROTOCOL,D1.ISIPV6DEV,\
    # #                         D1.CFGFILEDIR,D1.CFGFILENAME,D1.MGMTTYPE,\
    # #                         D1.FTPUSERNAME,D1.FTPPASSWORD,\
    # #                         decode(D1.SNMPPRIVPASSWORD,null,D1.SNMPPRIVPASSWORD,decrypt_data(D1.SNMPPRIVPASSWORD,?)) AS SNMPPRIVPASSWORD,\
    # #                         D1.osversion,D1.FITFLAG,D2.LOOPADDRESS AS MGMTLOOPADDRESS,D1.SNMPPORT,\
    # #                         decode(D1.SNDPASSWD,null,D1.SNDPASSWD,D1.SNDPASSWD,?)) AS SNDPASSWD,D1.PRIPWVALID,D1.SNDPWVALID\,D3.CARDCOLTYPE \
    # #                     FROM  DEVICE D1, DEVICE D2, DEVICEMODELLIB D3  \
    # #                     WHERE D1.DEVICEID IN 'deviceid' and D1.CHANGETYPE=0 and D1.MGMTDEVICEID = D2.DEVICEID(+) and NVL(D2.CHANGETYPE,0) = 0 and D1.DEVICEMODELCODE = D3.DEVICEMODELCODE(+)"
    # SQL = "select loopaddress,devicename from device where deviceid = :1"
    # args = [deviceid]
    # r=cur.execute(SQL,args)
    # #r=cur.fetchall()
    # r=cur.fetchone()
    # print(r)
    # cur.close()
    # conn.close()
    # result = {}
    # #result = {'loopaddress': r[0],'devicename': r[1]}
    # result['loopaddress'] = r[0]
    # result['devicename'] = r[1]

    #return jsonify({'mgmtip':'192.168.6.87','rocommunity':'public','devset':'DEV_R_CI_IOS','username':'aaa','passwd':'aaa'})

    args = [DString,DString,DString,DString,DString,DString,deviceid]
    SQL = "SELECT D1.DEVICEID,D1.DEVICENAME,D1.LOOPADDRESS,D1.PROMPT,D1.LOGINTYPE,D1.USERNAME,\
                            decode(D1.PASSWORD,null,D1.PASSWORD,decrypt_data(D1.PASSWORD,:1)) AS PASSWORD,\
                            decode(D1.ENABLEPASSWD,null,D1.ENABLEPASSWD,decrypt_data(D1.ENABLEPASSWD,:2)) AS ENABLEPASSWD,\
                            decode(D1.ROCOMMUNITY,null,D1.ROCOMMUNITY,decrypt_data(D1.ROCOMMUNITY,:3)) AS ROCOMMUNITY,\
                            D1.RWCOMMUNITY,\
                            D1.ISNEW,D1.DEVICETYPECODE,D1.DEVICEMODELCODE,D1.NODECODE,D1.DETAILMODELCODE,\
                            D1.SNMPVERSION,D1.SNMPUSERNAME,D1.SNMPAUTHPROTOCOL,\
                            decode(D1.SNMPAUTHPASSWORD,null,D1.SNMPAUTHPASSWORD,decrypt_data(D1.SNMPAUTHPASSWORD,:4)) AS SNMPAUTHPASSWORD,\
                            D1.SNMPPRIVPROTOCOL,D1.ISIPV6DEV,\
                            D1.CFGFILEDIR,D1.CFGFILENAME,D1.MGMTTYPE,\
                            D1.FTPUSERNAME,D1.FTPPASSWORD,\
                            decode(D1.SNMPPRIVPASSWORD,null,D1.SNMPPRIVPASSWORD,decrypt_data(D1.SNMPPRIVPASSWORD,:5)) AS SNMPPRIVPASSWORD,\
                            D1.osversion,D1.FITFLAG,D2.LOOPADDRESS AS MGMTLOOPADDRESS,D1.SNMPPORT,\
                            decode(D1.SNDPASSWD,null,D1.SNDPASSWD,D1.SNDPASSWD,:6) AS SNDPASSWD,D1.PRIPWVALID,D1.SNDPWVALID,D3.CARDCOLTYPE \
                        FROM  DEVICE D1, DEVICE D2, DEVICEMODELLIB D3 \
                        WHERE D1.DEVICEID = :7 and D1.CHANGETYPE=0 and D1.MGMTDEVICEID = D2.DEVICEID(+) and NVL(D2.CHANGETYPE,0) = 0 and D1.DEVICEMODELCODE = D3.DEVICEMODELCODE(+)"
    # SQL = "select loopaddress,devicename from device where deviceid = :1"
    result = pool_util_oracle.execute_query_single(SQL,dict_mark='Ture',args=args)
    return jsonify(json.dumps(result))