import os


def init():
    os.system("xrdb -load /dev/null")
    os.system("xrdb -query")
