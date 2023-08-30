print("\n*** Welcome to our Calculator App.***")
print("\n*** INSTRUCTION ***")
print('''
1) + for Addition.
2) - for Subtraction.
3) * for Multiplication.
4) / for Division.
''')

operators = ['+', '-', '*', '/']

def calculate(operator, num1, num2):
    if operator == '+':
        print(f"The result of {num1} {operator} {num2} = {num1 + num2}")
    elif operator == '-':
        print(f"The result of {num1} {operator} {num2} = {num1 - num2}")
    elif operator == '*':
        print(f"The result of {num1} {operator} {num2} = {num1 * num2}")
    elif operator == '/':
        if num2 != 0:
            print(f"The result of {num1} {operator} {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")

while True:
    operator = input("\nEnter the operator ('+', '-', '*', '/'): ")
    if operator in operators:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        calculate(operator, num1, num2)
        choice = input("Want to continue or not? (y/n): ")
        if choice.lower().endswith('n'):
            print("Thank you for using our calculator. Goodbye!")
    else:
        print("Invalid Input. Try Again.")