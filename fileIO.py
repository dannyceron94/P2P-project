# this file take care of writting file to the machine
import os
PATH_TO_FILE = "/read_file.txt"
PATH_TO_NEWFILE = "/new_file.txt"
cwd = os.getcwd()
path_to_file    = cwd + PATH_TO_FILE
path_to_newFile = cwd + PATH_TO_NEWFILE

def convert_to_bytes(path_to_file=path_to_file):
    data=None
    with open(path_to_file,'r') as file:
        data = file.read()
    return data.encode("utf-8")

def create_file(data):
    data = data.decode("utf-8")
    print("writing file to machine")
    with open(path_to_newFile,'w') as file:
        file.write(data)
    return True
def main():
    data = convert_to_bytes()
    create_file(data)

if __name__ == "__main__":
    main()