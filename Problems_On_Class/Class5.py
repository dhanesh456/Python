#Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest.
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.



class BankAccount:
    
    ROI = 10.5
    
    def __init__(self,UserName,CurrentAmount):
        self.Name = UserName      
        self.Amount = CurrentAmount
        
    def Deposit(self,Value):        
        self.Amount = self.Amount + Value
        return self.Amount
    
    def Withdraw(self,Value):
        self.Amount = self.Amount - Value
        return self.Amount
        
    def CalculateIntrest(self):
        Intrest = (self.Amount * 10.5 * 1)/100 
        return Intrest
        
    def Display(self):
        print("Name of Account holder : ",self.Name)
        print("Current Balance : ",self.Amount)  
        print("Rate of intrest : 10.5% ")    
        


def main():
    
    print("Enter your Full Name")
    Username = input()
    
    print("Enter an amount")
    CurrentAmount = int(input())
 
    obj = BankAccount(Username , CurrentAmount)
    
    print("--------------------------------------------")
    
    print("Enter the value you want to deposit")
    CreditAmmount = int(input())
    print("New Balance :",obj.Deposit(CreditAmmount))
    
    print("--------------------------------------------")
    
    print("Enter the value you want to Withdraw")
    DebitAmmount = int(input())
    print("New Balance :",obj.Withdraw(DebitAmmount))
    
    print("--------------------------------------------")
    
    obj.Display()
    print("Therefore intrest on Balance amount per year :",obj.CalculateIntrest())
        
    
if __name__ == "__main__":
    main()               