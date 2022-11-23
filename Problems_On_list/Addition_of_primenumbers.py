# Program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from list



def ChkPrime(num):
    result=True
    for i in range(2,num):
        if num%i==0:
            result=False
            break
    return result


def AddPrime(lst):
    Temp_list = []
    Addition=0
    for element in lst:
        if ChkPrime(element)==True:
            #print(element)
            Temp_list.append(element)
            Addition = Addition+element

    print("Prime numbers in list = ",Temp_list)
    return Addition

def main():
     
    List = []
    print("Enter count of element in array: ")
    NO_Element = int(input())
    
    print("Enter array elements : ")
    
    for i in range(0,NO_Element):
        List.append(int(input()))    
    
    iRet = AddPrime(List)
    
    print("Summation of all prime no in list is:",iRet)
    

       

if __name__ == "__main__":
    main()    