
#Normal function / Named functions 
#def Function_Name(Function_Parameters):


def Add(iNo1 ,iNo2):
    return iNo1+iNo2

#Lambda Functions /  Unnamed function
# lambda parameters : body
    
AddFunction = lambda A,B : A+B
def main():
    Ans1 = Add(10,11)
    Ans2 = AddFunction(11,22)

    print("Addition using normal function : ",Ans1)
    print("Addition using Lambda function : ",Ans2)
    print("Type of lambda function is : ",type(AddFunction))        


if __name__ == "__main__":
    main()