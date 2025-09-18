def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1-4): "))
            if choice in [1, 2, 3, 4]:
                break
            print("Please enter a valid choice (1-4)")
        except ValueError:
            print("Please enter a valid number")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"{num1} × {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"{num1} ÷ {num2} = {num1 / num2}")
        else:
            print("Error: Cannot divide by zero!")

calculator()