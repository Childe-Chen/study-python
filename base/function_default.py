# python 中好像没有方法重载，但是通过默认参数值可达到相同效果
# 在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。
# 这是因为值是按参数所处的位置依次分配的。举例来说，def func(a, b=5) 是有效的，但 def func(a=5, b) 是无效的。


def say(msg, times=2):
    print(msg * times)


say("hello", 3)
say("ha")
say(3)
