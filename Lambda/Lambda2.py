#Program which contains one lambda function which accepts two numbers
#And return its multiplication


Multiplication = lambda A , B : A*B

def main():
    print("Enter first value")
    iNo1 = int(input())

    print("Enter second value")
    iNo2 = int(input())

    iRet = Multiplication(iNo1,iNo2)
    print("Multiplication of two numbers is ",iRet)
if __name__ == "__main__":
    main()    