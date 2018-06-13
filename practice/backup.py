import os
import time
from practice import oszip
from practice import zip_file

# 待备份目录
sourceDir = ["/Users/childe/logs/bak"]

# 备份目录
targetDir = "/Users/childe/logs/zip"

# 目录检查
for path in sourceDir:
    if not os.path.exists(path):
        print("source dir not exists")
        exit(0)


if not os.path.exists(targetDir):
    os.mkdir(targetDir)

# 定义备份名称

targetName = time.strftime("%Y-%m-%d-%H-%M-%S")
target = targetDir + os.sep + targetName + ".zip"


def get_user_select():
    while True:
        print("================")
        print("select zip ways:")
        print("1.os zip")
        print("2.python zipfile")
        print("0.exit")
        user_input = input("enter a number:")

        if not user_input.isdigit():
            print("input the number of above!")
            continue
        user_input = int(user_input)
        if user_input > 2:
            print("input the number of above!")
            continue
        return user_input


# 打印备份方式选项
# 等待输入
select = get_user_select()

# 输入处理
if select == 0:
    exit(0)
elif select == 1:
    # 开始备份
    print("start backup")
    oszip.backup(sourceDir, target)
elif select == 2:
    # 开始备份
    print("start backup")
    zip_file.backup(sourceDir, target)
else:
    exit(1)


print("end backup")
