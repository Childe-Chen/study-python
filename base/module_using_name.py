# 若直接运行（独立运行）该文件，name为__main__
# 如果被其他模块import，其name默认为文件名

print(__name__)

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
