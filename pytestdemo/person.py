class Person:
    def get_name(self):
        return "hogwarts"


    def get_age(self):
        self.get_name()
        print("11")

    @classmethod
    def getmoney(self):
        return '1000'


Person().get_age()
