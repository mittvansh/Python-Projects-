import math     #Import Math Library so we can perform mathematical operations.
Result = 0.00
table = True
calculation_number = 0
total = 0.0
avg = 0.0
no_print = False        #Initialize Variables. 
while table:    #Start the while loop so the calculator runs multiple times
    if no_print:
        print()
    else:
        print("Current Result: " + str(Result) + "\n")
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Exponentiation\n"
            "6. Logarithm\n"
            "7. Display Average\n")
    operation = input("Enter Menu Selection: ")     #Printing Calculator menu
    print(" ")
    no_print = False
    if operation == "0":
        table = False
        print("Thanks for using this calculator. Goodbye!")
    elif operation == "1":
        num1 = (input("Enter first operand: "))
        num2 = (input("Enter second operand: "))  
        if num1 == "RESULT":
            num1 = float(Result)
        else:
            num1 = float(num1)
        if num2 == "RESULT":
            num2 = float(Result)
        else:
            num2 = float(num2)
        Result = num1+num2
        total += Result
        calculation_number += 1         #Do addition
    elif operation == "2":
        num1 = (input("Enter first operand: "))
        num2 = (input("Enter second operand: "))
        if num1 == "RESULT":
            num1 = float(Result)
        else:
            num1 = float(num1)
        if num2 == "RESULT":
            num2 = float(Result)
        else:
            num2 = float(num2)
        Result = num1-num2
        total += Result
        calculation_number += 1     #Do subtraction
    elif operation == "3":
        num1 = (input("Enter first operand: "))
        num2 = (input("Enter second operand: "))
        if num1 == "RESULT":
            num1 = float(Result)
        else:
            num1 = float(num1)
        if num2 == "RESULT":
            num2 = float(Result)
        else:
            num2 = float(num2)
        Result = num1*num2
        total += Result
        calculation_number += 1         #Do Multiplication
    elif operation == "4":
        num1 = (input("Enter first operand: "))
        num2 = (input("Enter second operand: "))
        if num1 == "RESULT":
            num1 = float(Result)
        else:
            num1 = float(num1)
        if num2 == "RESULT":
            num2 = float(Result)
        else:
            num2 = float(num2)
        Result = num1/num2
        total += Result
        calculation_number += 1         #Do Division
    elif operation == "5":
        num1 = (input("Enter first operand: "))
        num2 = (input("Enter second operand: "))
        if num1 == "RESULT":
            num1 = float(Result)
        else:
            num1 = float(num1)
        if num2 == "RESULT":
            num2 = float(Result)
        else:
            num2 = float(num2)
        Result = num1 ** num2
        total += Result
        calculation_number += 1         #Do Exponentiation
    elif operation == "6":
        num1 = (input("Enter first operand: "))
        num2 = (input("Enter second operand: "))
        if num1 == "RESULT":
            num1 = float(Result)
        else:
            num1 = float(num1)
        if num2 == "RESULT":
            num2 = float(Result)
        else:
            num2 = float(num2)
        Result = math.log(num2, num1)
        total += Result
        calculation_number += 1         #Do Logarithm
    elif operation == "7":
        no_print = True
        if calculation_number == 0:
            print("Error: No calculations yet to average!")
        else:
            print(f"Sum of calculations: {total}")
            print(f"Number of calculations: {calculation_number}")
            avg = total / calculation_number
            avg = round(avg, 2)
            print(f"Average of calculations: {avg}")        #Perform Average
    else:
        no_print = True
        print("\nError: Invalid selection!" + "\n")     #for when the user inputs a number that is less than 0 or greater than 7.