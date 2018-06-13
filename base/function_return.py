def func():
    return


# pass 语句用于指示一个没有内容的语句块
# Python 有一个甚是优美的功能称作文档字符串（Documentation Strings），在称呼它时通常会使用另一个短一些的名字docstrings。
# DocStrings 是一款你应当使用的重要工具，它能够帮助你更好地记录程序并让其更加易于理解。
# 令人惊叹的是，当程序实际运行时，我们甚至可以通过一个函数来获取文档！
def func1():
    """This method is empty"""
    pass


print(func())
print(func1())
print(func1.__doc__)

