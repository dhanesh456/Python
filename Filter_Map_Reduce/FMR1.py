
def CheckEven(No):
    if(No % 2 == 0):
        return True

def Multi(No):
    Sum = 0
    Sum = Sum * No
    return Sum

def Sum(A,B):
    return A + B


def reduceX(Helper_Function,Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,no)

    return Ans


def filterx(Helper_Function, Data):
    Result = []
    for no in Data:
        if (Helper_Function(no) == True):
            Result.append(no)
        return Result


def mapX(Helper_function,Data ):
    Result = []
    for No in Data:
        if(Helper_function(No)== True):
            Result.append(No)

    return Result
          



def main():
    print("Enter the number of elements you want to enter : ")

    iSize = int(input())

    Data_Input = []

    print("Please under the Data ")

    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Elements of Data_Input",Data_Input)

    Data_Filter = filterx(CheckEven , Data_Input)
    print("Data after filter is : ",Data_Filter)

    Data_map = mapX(Multi,Data_Filter)
    print("Data after map is : ",Data_map)

    Output = reduceX(Sum,Data_map)
    print("Result after reduce is : ",Output)

  
    
if __name__ == "__main__":
    main()    