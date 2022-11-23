# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square.
# Reduce will return addition of all that numbers

# Input list =  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter =  [2, 4, 4, 2, 8, 10]
# List after map  = [4, 16, 16, 4, 64, 100]
# Output of reduce =  204

def FilterX(List1):
    ListA = []

    for i in List1:
        if((i % 2) == 0):
            ListA.append(i)
    
    return ListA

def MapX(List2):
    ListB = []
    
    for value in List2:
        sum = value*value
        ListB.append(sum)
     
    return ListB

def ReduceX(List3):
    sum = 0
    for value in List3:
        sum = value + sum
    return sum    


def main():
    listX = []
    print("Enter number of elements you want to store in the list ")
    iValue1 = int(input())
    print("Enter values of elements")
    for i in range(0,iValue1):
        Input = int(input())
        listX.append(Input)
    print("Input list = ",listX)    

    iFilter = FilterX(listX)
    print("List after filter = ",iFilter)
    
    iMap = MapX(iFilter)
    print("List after map = ",iMap) 
    
    iReduce = ReduceX(iMap)
    print("Outpit of reduce = ",iReduce)
    
    
    
    

if __name__ == "__main__":
    main()    