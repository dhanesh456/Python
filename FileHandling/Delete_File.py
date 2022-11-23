import os


def Delete_File(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if size == 0:
            os.remove(FileName)
        else:
            print("Are you sure you want to delete the file? Y/N")
            Option = input()
            if(Option == "Y" or Option == "y"):    
                os.remove(FileName)
            else:
                print("File deletion process stopped ")    
    else:
        print("File is not existing ")
        return
def main():
    print("Enter the file name to delete ")
    Name = input()
    
    
    Delete_File(Name)
 
if __name__ == "__main__":
    main()