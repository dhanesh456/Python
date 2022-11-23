# Program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 
# And less than or equal to 90
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.4

# Input List = [7, 8, 6, 55, 88, 77]
# List after filter =  [88, 77]
# List after map =  [98, 87]
# Output of reduce :  8526



def FilterX(List1):
    valuesX = []

    for value in List1:
        if(value >= 70):
            if(value <=90):
                valuesX.append(value)
    return valuesX 
    
    mapX(valuesX)
    
def mapX(List2):
    valuesY = []
    for value in List2:
        Sum = value + 10
        valuesY.append(Sum)
    return valuesY

def ReduceX(List3):
    sum = 1
    for i in List3:
        sum = i * sum      
    return sum

def main():
    Xlist = []
    print("Enter number of element in the list :")
    ElementX = int(input())
    print("Enter values of elements")

    for i in range(0,ElementX):
        inputX = int(input())
        Xlist.append(inputX)
    print("Input List = ",Xlist)

    iFilter = FilterX(Xlist)
    print("List after filter = ",iFilter)
    
    iMap = mapX(iFilter)
    print("List after map = ",iMap)
    
    iReduce = ReduceX(iMap)
    print("Output of reduce : ",iReduce)
     

if __name__ == "__main__":
    main()    