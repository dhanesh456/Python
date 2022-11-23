# Program which contains filter(),map() and reduce() in it
# Python appliction which contain one list of number 
# List contains the number which are accepted from user
# Filter should filter out all prime numbers
# Map function will multiply each number by 2
# Reduce will return maximum number from that number

# List after filter =  [2, 11, 17, 23, 31]
# List after map =  [4, 22, 34, 46, 62]
# Output of reduce =  62



def ChkPrime(num):
    result=True
    for i in range(2,num):
        if num%i==0:
            result=False
            break
    return result

def PrimeList(List1):
    Elist = []
    for i in List1:
        if (ChkPrime(i)==True):
            Elist.append(i)
    return Elist
    
           
def Multiply(List2):
    MList = []
    mult = 0
    for i in List2:
        mult = i * 2
        MList.append(mult)
    return MList 

def Maximum(List3):
    max = 0
    for i in List3:
        if i > max:
            max = i
    return max
       
def main():
    InputList = []
    print("Enter number of Element : ")
    iElement = int(input())
    print("Enter values of element :")
    for i in range(0,iElement):
        iInput = int(input())
        InputList.append(iInput)
        
    FilterX = PrimeList(InputList)  
    print("List after filter = ",FilterX) 
    
    MapX = Multiply(FilterX)
    print("List after map = ",MapX) 
    
    ReduceX = Maximum(MapX)
    print("Output of reduce = ",ReduceX)
        
    
if __name__ == "__main__":
    main()    