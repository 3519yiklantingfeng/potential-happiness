import pytest
@pytest.mark.parametrize('key,result',[
    ['appium',200],['selenium',200],['request',200],['docker',300]],ids=['a','b','c','d'])
def test_interface(key,result):
    url = f'http://ceshiren.com/key={key}'
    print(url)



@pytest.mark.parametrize('a,b',[
    [1,1],[100,100]
])
class TestDemo:
    def test_a(self,a,b):
        print(a,b)
    def test_b(self,a,b):
        print(a,b)


@pytest.mark.parametrize('c',['x','y','z'])
@pytest.mark.parametrize('b',[1,2,3])
@pytest.mark.parametrize('a',['int','string','float'])
def test_ab(a,b,c):
    print(a,b,c)
