def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        case _:
            print("Invalid operation selected.")
            return
            
    print(f"The result is {result}")

if __name__ == "__main__":
    main()
