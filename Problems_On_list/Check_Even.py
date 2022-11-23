#To check whether the number is even 

def ChkNum():
    print("Please enter a value : ")
    No = int(input())

    if (No % 2) == 0 :
        print("The number is even")
    else:
        print("The number is odd")    


def main():
    ChkNum()

if __name__ == "__main__":
    main()
