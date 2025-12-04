import os, json, shutil, sys # adding all the necessary packages.
from subprocess import PIPE, run # this will help us in running the code in GOLang. 

GAME_DIR_PATTERN = "game" # this is just a global scope var

def find_all_game_dirs_paths(source): # a function to find all the dirs in the source dir that are game dirs
    game_paths = [] # a list that will eventually contain all the game dirs full paths
    
    for root, dirs, files in os.walk(source): # this loop will go through all the dirs and files in the root (source) dir but only once as we don't want to go through the whole dir tree
        for foundDirectory in dirs: # this will only take out all the dirs from the found files and dirs in the outer loop. 
            if GAME_DIR_PATTERN in foundDirectory.lower(): # this is a substring comparison if statement
                path = os.path.join(source, foundDirectory) # if 'game' is present in the dir name, then a temp path var will be created that will contain the full path of the game dir
                game_paths.append(path) # the full path in the temp path var will then be appended in the list created on line 7
        break
    
    pass

def main(source, target):
    # task 1
    cwd = os.getcwd() # this line will get the Current Working Directory and will save it to the cwd var.
    source_path = os.path.join(cwd, source) # this will join the path in cwd var to the file name in source var
    target_path = os.path.join(cwd, target) # this will join the path in cwd var to the file name in target var
    # test
    # print(source_path)
    # print(target_path)
    
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