import os, json, shutil, sys # adding all the necessary packages.
from subprocess import PIPE, run # this will help us in running the code in GOLang. 

def main(source, target):
    # task 1
    cwd = os.getcwd() # this line will get the Current Working Directory and will save it to the cwd var.
    source_path = os.path.join(cwd, source) # this will join the path in cwd var to the file name in source var
    target_path = os.path.join(cwd, target) # this will join the path in cwd var to the file name in target var
    # test
    print(source_path)
    print(target_path)
    
    return 0

if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 3:
        raise Exception("You must pass a source and a directory file to complete the action.") # that is how you add a custom exception.
    source, target = args[1:]
    # test
    # print(source, target)
    main(source, target)