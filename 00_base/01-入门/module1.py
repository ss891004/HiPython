

def addFunc(a,b):  
    return a+b  



if __name__=="__main__":
    print('test ：1+1的计算结果:',addFunc(1,1))

'''
一个python的文件有两种使用的方法：

1，直接作为脚本执行。
2，import到其他的python脚本(.py文件)中导入被作为模块调用执行。
if name == ‘main’: 的作用就是控制这两种情况执行代码的过程，在if name == ‘main’: 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中作为模块使用是不会被执行的。
'''


