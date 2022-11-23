# A program which accepts file name from user and create new file named as 
# demo.txt and copy all contents from existing file into new file.
# Accept file name through command line arguments

import os
from sys import argv



def CreateFile(FileName):
    
    if(os.path.exists(FileName)):
        print("File is already existing ")
        exit()
    else:
        Create = open(FileName, "w")
        return Create

def DataCopy(FileName):
    if(os.path.exists(FileName)):
        
        
        Old = open(FileName , "r")  # Opened the old file in read mode
        Data = Old.read()           # Took the Data from the file into a variable 
        
        
        print("Enter a new file name")
        FileNew = input()
        New = CreateFile(FileNew)       # Created a new file
        fd = open(FileNew , "a")        # Opened that file in append mode
        
        fd.write(Data)                  # Copied the data from the variable to the new file
        print("Successfully copied the data from "+FileName+ " to "+FileNew)

def main():
    print("Application to copy data from one file to another")
    
    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("Pass one file name")
        
        exit()

    if(argv[1] == "-u"):
        print("Usage : This application will copy the data from one file and paste it in a new file. ")
        exit()
                

    DataCopy(argv[1])
    
if __name__ == "__main__":
    main()    