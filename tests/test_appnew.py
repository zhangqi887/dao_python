#import sys
#sys.path.append("..")
from app1 import app
from flask import json,jsonify

class TestClass(object):
    def setup_class(self):
        """测试开始时候执行, 用来做准备工作，一般用来初始化资源。"""
        app.config['TESTING'] = True  # 这将会使得处理请求时的错误捕捉失效，以便于 您在进行对应用发出请求的测试时获得更好的错误反馈。
        # 测试客户端将会给我们一个通向应用的简单接口，我们可以激发 对向应用发送请求的测试，并且此客户端也会帮我们记录 Cookie 的 动态。
        self.app = app.test_client()

    def teardown_class(self):
        """测试结束时执行， 用来做收尾工作， 一般用来关闭资源"""
        pass

    def test_health(self):
        response = self.app.get('/health')
        #assert b'{\n  "status": "up"\n}\n' == response.data
        data=json.loads(response.data)
        assert  data== {'status':'up'}
        assert  data['status'] == 'up'

#    def test_logout(self):
#        response = self.app.get('logout')
#        assert b'logout' == response.data

    def test_index(self):
        response = self.app.get('/')
        assert b'Hello, World!' == response.data
        #assert b'hello' == response.data
        
    def test_test(self):
        response = self.app.get('/test')
        #assert b'{\n  "status": "up"\n}\n' == response.data
        data=json.loads(response.data)
        str=data['code']
        exec(str,globals(),locals())
        t1=locals()['t']
        assert t1()=='hello"<[{中文}]>"'
        #assert  data['状态'] == '正常'
