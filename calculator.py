while True:
    print("\n=== CALCULATOR ===")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Exit")

    option = input("Choose an option: ")

    if option == "0":
        print("Exiting...")
        break

    if option in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == "1":
            result = num1 + num2
            print("Result:", result)

        elif option == "2":
            result = num1 - num2
            print("Result:", result)

        elif option == "3":
            result = num1 * num2
            print("Result:", result)

        elif option == "4":
            if num2 != 0:
                result = num1 / num2
                print("Result:", result)
            else:
                print("Error: division by zero!")

    else:
        print("Invalid option!")
