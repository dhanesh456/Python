# Program which accepts file name from user and open that file
# and display the contents of that file

import os

def Read(FileName):
    if(os.path.exists(FileName)):
        Fd = open(FileName,"r")
        print("Data from this file")
        Data = Fd.read()
        print(Data)
        exit()
        
        
    else:    
        print("File does not exists")
        exit()


def main():
    
    print("Enter a file name you want to Read ")
    File = input()
    
    Read(File)
    
    
if __name__ == "__main__":
    main()    