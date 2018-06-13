# *表示数组，**表示字典（即Map）


def func(a, *numbers, **phone_book):
    print(a)
    for number in numbers:
        print(number, end="\t")

    print()

    for name, phone in phone_book.items():
        print("name={0}, phone={1}".format(name, phone))


func(1, 2, 3, 4, Jack=110, Mack=120)
