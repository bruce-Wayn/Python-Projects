print("Hi! welcome to Advanced calculator(non-scientific).\n"
      "AKA  \n"
      "Memory calculator\n"
      "easy-to use \n"
      "***note! If you want to clear the data enter c or C and the program will be ended once you input c as an operator \n"
      "Remember, if you enter any invalid operator the calculator will end \n"
      "Also! if you add a char in place of number input there will be error \n"
      "as you cannot add a number and a character type\n"
      "Operators used are: \n"
      "+, -, *, /, ^(for power function: works as num1^num2), c (used for clearing and ending program)")
def algo(num1, num2):
    opr = str(input("please enter the operator from the following: +, -, *, /, ^ (for power function: works as num1^num2), c (used for clearing and ending program)"))
    a = 0
    for a in range(0, 77777777,1):
        if (opr == "c"):                                                                #reading opr and then processing from commands below
            print("Ended!")
            break
        elif (opr == "C"):
            print("Ended!")
            break
        elif (opr == "end"):
            print("Ended!")
            break
        elif (opr == "End"):
            print("Ended!")
            break
        elif (opr == "END"):
            print("Ended!")
            break
        elif (opr == "bye"):
            print("Goodbye!")
            break
        elif (opr == "Bye"):
            print("Goodbye!")
            break
        elif (opr == "BYE"):
            print("Goodbye!")
            break
        elif (opr == "+"):
            num2 = float(input("please enter the next number to operate with"))         #now after inserting value into num2
        elif (opr == "-"):
            num2 = float(input("please enter the next number to operate with"))         #if we type c or C or non operators, the program will end immediately without asking for num2 value
        elif (opr == "*"):
            num2 = float(input("please enter the next number to operate with"))
        elif (opr == "/"):
            num2 = float(input("please enter the next number to operate with"))
            if(num2 == 0):
                print("Invalid! please write any number for denominator except 0")
                num2 = float(input("please enter the next number to operate with"))
        elif (opr == "^"):
            num2 = float(input("please enter the next number to operate with"))
        else:
            print("invalid input please retry!")
            break       #num2 algorithm ended here


#this will work if we finally added value to num2, or it will end if operatos are c, C or not defined. Thus making a closed loop in terms of opr and num2
        if(opr == "+"):
            num1 = num1+num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
        elif(opr == "-"):
            num1 = num1-num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
        elif(opr == "*"):
            num1 = num1*num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
        elif(opr == "/"):
            num1 = num1/num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
        elif(opr == "c"):
            break
        elif(opr == "C"):
            break
        elif(opr == "^"):
            print("here your input number: " , num1," is base and input number: ",num2," is power")
            num1 = pow(num1,num2)
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
        else:
            print("Invalid operator! Please try again and enter a valid operator amongst : +, -, *, /, c")
            break
num1 = float(input("enter 1st number: "))
num2 = 0
print(algo(num1, num2))

#i cant't believe i made this code
#worked on a previous code which was about 150 lines long and i shortened it to 60 lines code by just 1 if statement
#here is my previous code
#still working on the input error for num1 and num2 when a character is inserted
"""
def algo(num1, num2):
    opr = str(input("please enter the operator from the following: +, -, *, /, ^ (for power function: works as num1^num2), c (used for clearing and ending program)"))
    a = 0
    for a in range(0, 77777777,1):
        if(opr == "+"):
            num1 = num1+num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
            if(opr == "c"):
                break
            elif(opr == "C"):
                break
            elif(opr == "+"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "-"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "*"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "/"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            else:
                print("invalid input please retry!")
                break
        elif(opr == "-"):
            num1 = num1-num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
            if(opr == "c"):
                break
            elif(opr == "C"):
                break
            elif(opr == "+"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "-"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "*"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "/"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            else:
                print("invalid input please retry!")
                break
        elif(opr == "*"):
            num1 = num1*num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
            if(opr == "c"):
                break
            elif(opr == "C"):
                break
            elif(opr == "+"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "-"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "*"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "/"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            else:
                print("invalid input please retry!")
                break
        elif(opr == "/"):
            num1 = num1/num2
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
            if(opr == "c"):
                break
            elif(opr == "C"):
                break
            elif(opr == "+"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "-"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "*"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "/"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            else:
                print("invalid input please retry!")
                break
        elif(opr == "c"):
            break
        elif(opr == "C"):
            break

        elif(opr == "^"):
            print("here your number 1 is base and number 2 is power")
            num1 = pow(num1,num2)
            print(num1)
            opr = str(input("please enter the next operator from the following: +, -, *, /, ^, c (used for clearing)"))
            if (opr == "c"):
                break
            elif (opr == "C"):
                break
            elif (opr == "+"):
                num2 = float(input("please enter the next number to operate with"))
            elif (opr == "-"):
                num2 = float(input("please enter the next number to operate with"))
            elif (opr == "*"):
                num2 = float(input("please enter the next number to operate with"))
            elif (opr == "/"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            else:
                print("invalid input please retry!")
                break
        else:
            opr = str(input("Invalid! Please enter a valid operator amongst : +, -, *, /, c"))
            if(opr == "c"):
                break
            elif(opr == "C"):
                break
            elif(opr == "+"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "-"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "*"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "/"):
                num2 = float(input("please enter the next number to operate with"))
            elif(opr == "^"):
                num2 = float(input("please enter the next number to operate with"))
            else:
                print("invalid input please retry!")
                break
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
print(algo(num1, num2))
"""
