# Accept file name and one string from user and
# return the frequency of that word from file


import os
from sys import *

def Count_String(FileName , String):
    
    Count = 0
    if(os.path.exists(FileName)):
        fd = open(FileName , "r")
        lines= fd.readlines()
        for line in lines:
            for word in line.split():
                if(word == String):
                    Count = Count+1
        
    else:
        print("There is no such file in the directory")
        exit()   
            
    return Count

def main():
    print("String frequency application")

    if(len(argv) < 3):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("Enter a file name and a string")
        exit()

    if(argv[1] == "-u"):
        print("Usage : To find frequency for the given string in the file")
        exit()

    iret = Count_String(argv[1] , argv[2])
    print("Frequency of "+argv[2]+" is ",iret)
if(__name__ == "__main__"):
    main()