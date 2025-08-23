def calulator(input1, input2, operation):
    if operation == '+':
        return input1 + input2
    elif operation == '-':
        return input1 - input2
    elif operation == '*':
        return input1 * input2
    elif operation == '/':
        if input2 != 0:
            return input1 / input2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        return input1 % input2
    elif operation == '**':
        return input1 ** input2
    elif operation == '//':
        if input2 != 0:
            return input1 // input2
        else:
            return "Error: Division by zero" 
    else:
        return "Error: Invalid operation"

input1=float(input("Enter first number: "))
input2=float(input("Enter second number: "))
print("Enetr Operation : ") 
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")
print("7. Floor Division (//)")
operation = input("Enter operation (+, -, *, /, %, **, //): ")
reuslt = calulator(input1, input2, operation)
print("Result: ",reuslt)