number = 16

stop = False
# 非逻辑用not
while not stop:
    guess = float(input("input a number: "))
    if guess == number:
        print("guess right")
        stop = True
    elif guess > number:
        print("guess more than number")
    else:
        print("guess less than number")

else:
    # 退出while是会执行
    print('The while loop is over.')
print('Done one')


while True:
    guess = float(input("input a number: "))
    if guess == number:
        print("guess right")
        break
    elif guess > number:
        print("guess more than number")
    else:
        print("guess less than number")
else:
    # 退出while是会执行
    print('The while loop is over.')
print('Done two')