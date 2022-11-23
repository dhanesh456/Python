#Program which contains one lambda function which accepts one paramenter
#And return power of two (Square Root)
#Input : 4
#Output : 16


Square = lambda A : A*A

def main():
    print("Enter a value who's square you want to find : ")
    iNo = int(input())

    iRet = Square(iNo)
    print("Square root of ",iNo,"is",iRet)    


if __name__ == "__main__":
    main()    