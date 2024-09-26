# Calculator Program 
# Input two numbers and an operation choice.
# 15 May 2024



print("\n========== Calculator ==========\n")

number1     = int(input("Enter 1st number      :  "))
number2     = int(input("Enter 2nd number      :  "))
operation   = input("\nOperation ( + - * /)  :  ") 

op_result   = 0


# function to print result
def result(num1, num2, op):     

    print("\n================================")
    print(str(num1), op, str(num2) + " = " + str(round(op_result)))
    print("================================")


# operations to perform calculations based on selected operator
if operation == "+":
    op_result = number1 + number2
    result(number1, number2, operation)

elif operation == "-":
    op_result = number1 - number2
    result(number1, number2, operation)

elif operation == "*":
    op_result = number1 * number2
    result(number1, number2, operation)
    

elif operation == "/":
    op_result = number1 / number2
    result(number1, number2, operation)

else:
    print("Invalid operator.")
