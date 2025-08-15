while True:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    op=input("Choose your Operation(+,-,/,*): ")

    if (op=="+"):
        res=num1+num2
        
    elif (op=="-"):
        res=num1-num2

    elif (op=='/'):

        res=num1/num2

    elif(op=='*'):
        if num2==0:
            print("You cannot give {num2}")
        res=num1*num2

    else:
        print("INVALID OPERATOR CHOOSE FROM THE GIVEN OPERATORS") 
        continue 

    print(f"{num1} {op} {num2} = {res}")  

    choice=input("Do You Want to Continue(y/n)")
    if choice.lower()!="y" or choice.lower()!="n":
        print("Enter y or n")
        
    if choice.lower()!= "y":
        print("Calculator closed")
        break