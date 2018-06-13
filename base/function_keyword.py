# 我们不再需要考虑参数的顺序，函数的使用将更加容易
# 我们可以只对那些我们希望赋予的参数以赋值，只要其它的参数都具有默认参数值


def func(a, b=1, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))


func(0)

func(0, 2)

func(1, c=8)

func(b=4, c=5, a=6)