#!/bin/env python3
from gevent.pywsgi import WSGIServer
from app1 import app
import logging        #引入日志模块
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.debug(__name__)
logger.debug(__package__)

def run():
    logger.debug("Serving on 5000...")
	
def test_run():
	run()
	

if __name__ == '__main__':
    test_run()
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()