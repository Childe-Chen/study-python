import zipfile
import os


def backup(source, target):
    with zipfile.ZipFile(target, mode='w', compression=zipfile.ZIP_LZMA) as zf:
        add_file(source, zf)
        zf.close()


def add_file(source, zf):
    if isinstance(source, str):
        print("add file", source)
        zf.write(source)
        return

    for file in source:
        if not os.path.exists(file):
            continue
        if os.path.isfile(file):
            print("add file", file)
            zf.write(file)
        elif os.path.isdir(file):
            files = os.listdir(file)
            for inte_file in files:
                add_file(file + os.sep + inte_file, zf)


__version__ = "0.1"
