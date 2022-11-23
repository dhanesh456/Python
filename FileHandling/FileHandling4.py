# A program which accept two file from user and compare contents of both the file
#  If both file contains same contents then display success otherwise display failure
# Accept names of both the files from command line



import os 
from sys import argv

def Compare(File1 ,File2):
    if(os.path.exists(File1)):
        
        if(os.path.exists(File2)):
            
            
            fd = open(File1 ,"r")
            Data = fd.read()
            
            fd2 = open(File2 ,"r")
            Data2 = fd2.read()
            
            
            if(Data == Data2):
                print("Data is same :Success")
            else:
                print("Data is different : Failure ")
                
    else:
        print("File doesn't exist in the directory")  
        exit()              
        


def main():
    print("-----------------Application to compare data from to file-----------------")
    
    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()
    if(argv[1] == '-h'):
        print("Enter two file name after program name")
        exit()
        
            
    Compare(argv[1],argv[2])
    
    
    
    
    
    
if __name__ == "__main__":
    main()    