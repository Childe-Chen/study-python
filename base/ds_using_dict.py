dic = {
    "name": "Jack",
    "age": 12,
    "sex": "man",
    "address": "sun"
}

print("Jack info len", len(dic))

print("Jack info", dic)

del dic["address"]

print("Jack info", dic)

for item, value in dic.items():
    print(item, value)


print("Jack level", dic.get("level"))

if dic.get("level") is None:
    dic["level"] = 4


print("Jack level", dic.get("level"))

