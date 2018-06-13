def func(a):
    print("a : ", a)
    a = 555
    print("change local a to : ", a)


param = 1
print("param is : ", param)

func(param)
print("after call func, param is : ", param)
