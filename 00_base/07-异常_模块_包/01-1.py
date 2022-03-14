try:
    printCount(80)
except ValueError:
    print("捕获到了")
except NameError:
    print("捕获到了NameError")
else:
    print("没有被捕获的异常时，我会执行的")
finally:
    print("我一定会执行的")