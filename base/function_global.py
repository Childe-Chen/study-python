def func(a):
    print("a : ", a)
    global param
    global param_g
    param_g = 2
    param = 111
    a = 555
    print("change local a to : ", a)


param = 1
print("param is : ", param)

func(param)
print("after call func, param is : ", param)
print("after call func, param_g is : ", param_g)

