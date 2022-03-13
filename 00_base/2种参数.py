'''
args 是 arguments 的缩写，表示位置参数；
kwargs 是 keyword arguments 的缩写，表示关键字参数。
并且*args 必须放在 **kwargs的前面，因为位置参数在关键字参数的前面。
'''

# *args 参数
def test_args(first, *args):
    print('first params: ', first)
    print(type(args))
    print(args)
    for v in args:
        print ('args argument: ', v)
print("--------------------------------------")
test_args(1, 2, 3, 4)
print("--------------------------------------")
test_args(1, {'dict_key1': 1, 'dict_key2': 2})

# 第一个参数是必须要传入的参数，所以使用了第一个形参，而后面三个参数则作为可变参数元组传入了实参，并且是作为元组tuple来使用的。
# 当第二个参数为字典时，会把字典整体当做一个元组传入实参。作为元组tuple来使用。


# **kwargs 参数
def test_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)
   print(type(kwargs))
   print(args)
   print(kwargs)
   for v in args:
      print ('ars argument (args): ', v)
   for k, v in kwargs.items():
      print ('kwargs argument %s (kwargs): %s' % (k, v))

print("--------------------------------------")
test_kwargs(1, 2, 3, 4, k1=5, k2=6)
print("--------------------------------------")
test_kwargs(1, 2, 3, 4, **{"k1": 5, "k2":6})

# 调用函数
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)