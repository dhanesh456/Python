# A python application which contains two threads named as thread1 and thread2
# Thread1 displays 1 to 50 on screen and thread2 will display 50 to 1
# in reverse order on screen. After execution of thread1 gets completed then schedule thread2

import threading

def Display():
    
    print("Normal order : ")
    for i in range(1,51):
       print(i)
    print("--------------------------------")        


def DisplayReverse():
    
    print("Reverse order : ")
    for i in range(50 ,1,-1):
        
        print(i)        

def main():
    
    t1 = threading.Thread(target= Display,)
    t2 = threading.Thread(target= DisplayReverse,)
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
if __name__ == "__main__":
    main()    