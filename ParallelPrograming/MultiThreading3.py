# A python application which creates two thread named as evenlist and oddlist
# Both the thread accepts list of integers as parameter
# Evenlist thread will add all even elements from input list and display its addition
# Oddlist thread will add all Odd elements from input list and display its addition

import threading

def EvenAdd(Arr):
    sum = 0
    for i in Arr:
        if(i % 2 == 0):
            sum = sum + i
    print("Addition of even number from list is : ",sum)

def OddAdd(Arr):
    sum = 0
    for i in Arr:
        if(i % 2 != 0):
            sum = sum + i
    print("Addition of even number from list is : ",sum)
    

def DisplayOdd(No):
    for i in range(1,No,2):
        if(i % 2 != 0):
            print("Odd number = ",i)
    

def main():
    
    lst = []
    print("Enter number of element you want to store in the list")
    Element = int(input())
    for i in range(0,Element):
        i = int(input())
        lst.append(i)
    print(lst)    
    
    Evenlist = threading.Thread(target= EvenAdd, args=(lst,)) 
    Oddlist = threading.Thread(target= OddAdd, args=(lst,)) 
    
    Evenlist.start()
    Oddlist.start()
    
    Evenlist.join()
    Oddlist.join()
    

if __name__ == "__main__":
    main()    