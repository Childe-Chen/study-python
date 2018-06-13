poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

file_path = "/Users/childe/logs/poem.txt"
f = open(file_path, mode="w", encoding="utf-8")

try:
    f.write(poem)
finally:
    f.close()


f = open(file_path, mode="r", encoding="utf-8")

try:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")

finally:
    f.close()

