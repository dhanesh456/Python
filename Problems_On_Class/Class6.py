# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors), Factors).
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.



#Input : 69

# Output : 69 is not a prime number

# Output : Factors of 69 are :  [1, 3, 23]

# Output : Addition of factors are :  27

# Output : 69 is not a perfect number



class Numbers:
    def __init__(self,UserValue):
        self.No = UserValue
        
    def ChkPrime(self):
        result = True
        for i in range(2,self.No):
            if self.No % i == 0:
                result = False
                break
        return result
    def Factor(self):
        lst = []
        for i in range(1,int(((self.No/2)+1) )):
            if (self.No % i == 0):
                lst.append(i)
        return lst               
    def SumFactors(self):
        isum = 0
        for i in range(1,int(((self.No/2)+1) )):
            if(self.No % i == 0):
                isum = isum + i
        return isum 
    def CheckPerfect(self):
        Ans = self.SumFactors
        if(Ans == self.No):
            return True
              

def main():
    print("Enter a value : ")
    iNo = int(input())
    obj = Numbers(iNo)
    print("__________________________________________________")
    iRet = obj.ChkPrime()    
    if(iRet == True):
        print("{} is a prime number".format(iNo))
    else:
        print("{} is not a prime number".format(iNo))  
    
    print("__________________________________________________")
    
    iRet2 = obj.Factor()
    print("Factors of {} are : ".format(iNo),iRet2) 
    print("__________________________________________________")
    iRet3 = obj.SumFactors()
    print("Addition of factors are : ",iRet3)
    print("__________________________________________________")
    iRet4 = obj.CheckPerfect()
    if(iRet4 == True):
        print("{} is a perfect number ".format(iNo))
    else:
        print("{} is not a perfect number ".format(iNo))
        
        
    
    
if __name__ == "__main__":
    main()    