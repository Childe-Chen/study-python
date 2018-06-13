# 推荐使用括号来声明tuple
zoo = ("python", "monkey", "elephant")

print("Zoo number of animal", len(zoo))

# 定位tuple元素下标
print(zoo.count("monkey"))

print("old zoo are", zoo)

# tuple可嵌套tuple
new_zoo = ("cat", zoo)

print("new zoo are", new_zoo)
# 嵌套tuple的访问方式
print("new_zoo[1][2]", new_zoo[1][2])

# isinstance判断实例类型
for animal in new_zoo:
    if isinstance(animal, tuple):
        for animalO in animal:
            print(animalO)
    else:
        print(animal)

