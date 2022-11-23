
def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False  

def CheckEvenX(No):                            
    return (No % 2 == 0)

Even = lambda No : No % 2 == 0               # LAmbda 


print("Enter a number to check if its odd or even")
Value = int(input())
ret = CheckEvenX(Value)

if(ret == True):
    print("The given number is Even")
else:
    print("The given number is Odd")    