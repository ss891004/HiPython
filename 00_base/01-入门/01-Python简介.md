# 目标

- 了解Python
- Python的应用领域
- Python的版本

# Python介绍

Python是时下最流行、最火爆的编程语言之一，具体原因如下：

1. 简单、易学，适应人群广泛
2. 免费、开源
3. 应用领域广泛

> 备注：以下知名框架均是Python语言开发。

- Google开源机器学习框架：TensorFlow
- 开源社区主推学习框架：Scikit-learn
- 百度开源深度学习框架：Paddle

# Python版本

- Python 2.X
- Python 3.X
  - Python 3.5
  - Python 3.6
  - Python 3.7 

# 总结

- Python优点：
  - 学习成本低
  - 开源
  - 适应人群广泛
  - 应用领域广泛
- Python学习版本：3.7


# python 安装

# python 虚拟环境
```
1.创建一个虚拟环境
D:\>mkdir test_venv
D:\>cd test_venv
D:\test_venv>python -m venv test

注意命令python -m venv test,创建一个test的虚拟环境，生成目录形式如下：
test
  │  pyvenv.cfg
  ├─Include
  ├─Lib
  └─Scripts

2.启用虚拟环境
D:\test_venv>test\Scripts\activate.bat
(test) D:\test_venv>

执行那个activate.bat文件，启用后，提示符前面会出现虚拟环境的名字(test)。

3.pip在虚拟环境安装模块
(test) D:\test_venv>pip list

4.退出虚拟环境
(test) D:\test_venv>test\Scripts\deactivate.bat
```
