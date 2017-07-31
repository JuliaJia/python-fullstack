class Foo(object):
    def __init__(self):
        self.name = 'abc'
    def func(self):
        return "ok"



obj = Foo()
ret = getattr(obj,'name')
ret2 = setattr(obj,'name',"test")
ret = getattr(obj,'name')
# r = ret()
# print(r)

print(ret)