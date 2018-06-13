import pickle


file_path = "/Users/childe/logs/shoplist.data"

shop_list = ['apple', 'mango', 'carrot']

f = None
try:
    f = open(file_path, mode="wb")
    pickle.dump(shop_list, f)
finally:
    if f:
        f.close()


del shop_list

# with...as 会获取由 open 语句返回的对象，在本案例中就是“thefile”。
# 它总会在代码块开始之前调用 thefile.__enter__ 函数，并且总会在代码块执行完毕之后调用 thefile.__exit__。
# 等价于 try..finally 的语法糖
with open(file_path, mode="rb") as f:
    store_list = pickle.load(f)

print(store_list)

