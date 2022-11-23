# A program which accepts file name from user and check whether that file exists in current directory or no

import os

def Search(FileName):
    if(os.path.exists(FileName)):
        print("File exists in the current directory")
        
    else:    
        print("File does not exists in the current directory")


def main():
    
    print("Enter a file name you want to search ")
    File = input()
    
    Search(File)
    
    
if __name__ == "__main__":
    main()    