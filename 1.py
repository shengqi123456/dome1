# 装饰器
# import time
# def qwe(fn):
#     def ineer(*args,**kwargs):
#         s=time.time()
#         ret=fn(*args,**kwargs)
#         e=time.time()
#         print(f"所用的时间是{e-s}")
#         return ret
#     return ineer()
# @qwe
# def ll():
#     n=0
#     for i in range(1000000):
#         n+=i
#     return n
#
# s=ll()
#单利模式
class Mydata:
    _log=None
    def __new__(cls, *args, **kwargs):
        cls._log=object.__new__(cls)
        return cls
ll=Mydata()
ls=Mydata()
print(id(ll))
print(id(ls))

