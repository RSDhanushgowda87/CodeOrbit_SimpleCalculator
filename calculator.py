def calculator():
    # Display the available arithmetic operations to the user
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    try:
        # Take user input for the operation choice and operands
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid Input: Please choose a valid menu option.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected arithmetic operation and display results clearly
        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == '4':
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")

    # Handle invalid inputs such as division by zero and non-numeric values using try/except
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")

# Execute the calculator function
calculator()
