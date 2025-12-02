import os, json, shutil, sys # adding all the necessary packages.
from subprocess import PIPE, run # this will help us in running the code in GOLang. 

def main():
    return 0

if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 3:
        raise Exception("You must pass a source and a directory file to complete the action.") # that is how you add a custom exception.
    source, target = args[1:]
    # test
    # print(source, target)
    # main()