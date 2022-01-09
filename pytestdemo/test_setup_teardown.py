def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_case1():
    print("case1")

class TestDemo:
# 执行类 前后分别执行set_class   teardown_class
    def setup_class(self):
        print('TestDemo setup_class')
    def teardown_class(self):
        print('TestDemo taerdown_class')
    #每个类里面的方法前后分别执行setup，teardown
    def setup_class(self):
        print('TestDemo setup')
    def teardown_class(self):
        print('TestDemo taerdown')
