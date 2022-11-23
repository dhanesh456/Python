#Program which accept N number from user and store 
#it into a List .Return Addition of all elements from that list
#Input : Number of elements : 6
#Input Elements : 13, 5, 45, 7, 4 ,56
#Output : 130

def Add(values):
    sum = 0

    for no in values:
        sum = sum + no
    return sum


def main():

    arr = list()
    print("Enter the number of element you want to store in the list")
    iNo = int(input())

    print("Enter the values")
    for i in range(0,iNo):
        iValues = int(input())
        arr.append(iValues)

    print("Values of the list : ",arr)

    iRet = Add(arr)
    print("Addition of all elements from the list is :  ",iRet)



if __name__ == "__main__":
    main()    