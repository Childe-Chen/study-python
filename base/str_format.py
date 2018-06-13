name = "childe"
age = 28

intro = "{0} is a man, he is {1} years old"

# format 方法所做的事情便是将每个参数值替换至格式所在的位置
print(intro.format(name, age))

# 浮点数精度
num = 1/3

intro = "精确到小数点后4位 {0:.4f}"
print(intro.format(num))

intro = "精确到小数点后0位 {0:.0f}"
print(intro.format(num))

# 使用特定字符填充文本，并保持文字处于中间位置
hello = "hello"

intro = "前缀后缀 {0:-^11}"
print(intro.format(hello))

# 基于关键词输出
intro = "{name} is a man, he is {age} years old"
print(intro.format(name=name, age=age))
print(intro.format(name="huajiao", age=28))

# print 默认以换行结束，可使用end修改结束字符
print("first line")
print("second line")

print("first line", end="\t")
print("second line")

# 转义序列
print("second ' line")


# 比较  用==也可比较，似乎与Java不同
a = "q"
b = "qw"

print(a.__eq__(b))
