num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operation=input("Enter the operation: (+, -, *, /, %, **)\n")
if operation == "+":
    print(f"the result: {num1 + num2}")
elif operation == "-":
    print(f"the result: {num1 - num2}")
elif operation == "*":
    print(f"the result: {num1 * num2}")
elif operation == "/":
    print(f"the result: {num1 / num2}")
elif operation == "%":
    print(f"the result: {num1 % num2}")
elif operation == "**":
    print(f"the result: {num1 ** num2}")
else:
    print("this operation not available.")
