# A python application which creates two thread named as evenfactor and oddFactor
# Evenfactor thread will display Addition of even factor of given number and
# Oddfactor thread will display Addition of Odd factor of given number


import threading

def EvenFactor(No):
    Sum = 0
    
    for i in range(2,No,2):
        if(No % i == 0):
            Sum = Sum + i        
    print("Addition of Even factors is :",Sum)
    
def OddFactor(No):
    Sum = 0
    
    for i in range(1,No,2):
        if(No % i == 0):
            Sum = Sum + i        
    print("Addition of Odd factors is :",Sum)    

def main():
    print("Enter a number to find its sum of Even and Odd factor")
    Number = int(input())
    
    EvenT = threading.Thread(target= EvenFactor, args=(Number,))
    OddT = threading.Thread(target= OddFactor, args=(Number,))

    EvenT.start()
    OddT.start()
    
    EvenT.join()
    OddT.join()
    
    print("End of main")

if __name__ == "__main__":
    main()    