#相加功能
import pytest

from pytestdemo.Calculator import Calculator


def add(a,b):
    return a+b

class TestCal:

    print("setup")
    def setup_class(self):
        print("setup")


        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")
    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[0.1,0.1,0.2],[1000,1000,2000],[0,1000,1000]
    ],ids=['int1','float','bignum','zeronum'])
    def test_add(self,a,b,expect):
        # calc = Calculator()
        assert expect == self.calc.add(a,b)
    # def test_add1(self,a,b,expect):
    #     # calc = Calculator()
    #     assert expect == self.calc.add(0.1,0.1)
    # def test_add2(self,a,b,expect):
    #     # calc = Calculator()
    #     assert expect == self.calc.add(1000,1000)
    # def test_add3(self,a,b,expect):
    #     # calc = Calculator()
    #     assert expect == self.calc.add(0,1000)


