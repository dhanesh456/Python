#Program which accept N number from user and store it into List
#Return Minimum number from that list
#Input : Number of elemets : 4
#Input Elements : 13 5 45 7
#Output : 5


def Minimum(iValue):
    Min = iValue[0]
    for i in range(1,len(iValue)):
        if iValue[i] < Min:
            Min = iValue[i]
    return Min

def main():
    
    list2 = list()
    
    print("Enter number of elements you want to store in the list : ")
    
    iValue = int(input())
    
    print("Enter values of element ")
    
    for i in range(0,iValue):
        
        iInput = int(input())

        list2.append(iInput)

    print("Values of list : ",list2)

    
    iAns = Minimum(list2)
    
    print("Minimum number from list : ",iAns)    



if __name__ == "__main__":
    main()    