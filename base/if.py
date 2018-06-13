number = 23
guess = int(input("inter a num: "))

if guess == number:
    print("guess right")
elif guess > number:
    print("guess more than number")
else:
    print("guess less than number")

print("done")
