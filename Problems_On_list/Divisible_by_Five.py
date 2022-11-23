# To  Check whether the given number is divisible by 5 


def check(Value):
   
    if (Value % 5) == 0:
        print("True")
    else:
        print("False")    

def main():

    print("Enter a value")

    No = int(input())
    
    check(No)

if __name__ == "__main__":
    main()

