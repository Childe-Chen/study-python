import os


def backup(source, target):
    source_delimiter = " "
    archive = source_delimiter.join(source)
    command_template = "zip -r {archive} {inpath}"
    command = command_template.format(archive=target, inpath=archive)
    print(command)
    os.system(command)


__version__ = "0.1"
