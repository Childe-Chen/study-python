# 约定：任何在类或对象之中使用的变量其命名应以下划线开头，其它所有非此格式的名称都将是公开的，并可以为其它任何类或对象所使用。
# 请记得这只是一个约定，Python 并不强制如此（除了双下划线前缀这点）。


class Person:
    # 双下划线开头为私有，如果出现以双下划线结尾则失效
    __num = 0

    def __init__(self, name):
        self.name = name
        print("init person", name)
        Person.__num += 1

    def say_hi(self):
        print("hi from", self.name)

    @classmethod
    def how_many(cls):
        return cls.__num


class Man(Person):
    __man_num = 0

    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age
        Man.__man_num += 1

    def say_hi(self):
        print("hi from man", self.name)

    @classmethod
    def how_many(cls):
        return cls.__man_num


class Woman(Person):
    __woman_num = 0

    def __init__(self, name, hair):
        Person.__init__(self,name)
        self.hair = hair
        Woman.__woman_num += 1

    @classmethod
    def how_many(cls):
        return cls.__woman_num


man = Man("Jack", 12)
man1 = Man("Mack", 13)

woman = Woman("hanmeimei", "long")
woman1 = Woman("jer", "short")

print("Person num", Person.how_many())
print("Man num", Man.how_many())
print("Woman num", Woman.how_many())

personlist = [man, man1, woman, woman1]

for p in personlist:
    p.say_hi()
