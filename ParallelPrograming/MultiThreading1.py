# A python application which creates two thread named as even and odd
# Even thread will display first 10 even numbers and
# Odd thread will display first 10 odd numbers


import threading

def DisplayEven(No):
    for i in range(2,No,2):
        if(i % 2 == 0):
            print("Even number = ",i)
            
            
def DisplayOdd(No):
    for i in range(1,No,2):
        if(i % 2 != 0):
            print("Odd number = ",i)
    

def main():
    Number = 10
    
    Even = threading.Thread(target= DisplayEven, args=(Number,)) 
    Odd = threading.Thread(target= DisplayOdd, args=(Number,)) 
    
    Even.start()
    Odd.start()
    
    Even.join()
    Odd.join()
    

if __name__ == "__main__":
    main()    