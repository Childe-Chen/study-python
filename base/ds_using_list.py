shopList = ["apple", "banana", "mango", "carrot"]

print("I have", len(shopList), "items to purchase")

print("items are:", end=" ")
for item in shopList:
    print(item, end=" ")


print("I also have to buy rice.")
shopList.append("rice")

print("My shopping list is now", shopList)

print("sort my list")
shopList.sort()
print("My shopping list is now", shopList)

print("remove apple")
shopList.remove("apple")
print("My shopping list is now", shopList)

# 切片是一个新的引用
sublist = shopList[0:1]
sublist[0] = "www"
print(sublist)

print("My shopping list is now", shopList)

# 我们使用切片功能翻转文本。我们已经了解了我们可以通过使用 seq[a:b] 来从位置 a 开始到位置 b 结束来对序列进行切片 。
# 我们同样可以提供第三个参数来确定切片的步长（Step）。默认的步长为 1，它会返回一份连续的文本。
# 如果给定一个负数步长，如 -1，将返回翻转过的文本。
sublist = shopList[::-1]
print("reverse list", sublist)

# copy也是一个新的引用
newList = shopList.copy()

print("new list", newList)

newList.remove("rice")
newList[0] = "1111"

print("new list", newList)
print("old list", shopList)



