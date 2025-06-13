# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F = {converted:.2f}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C = {converted:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Error: Invalid temperature. Please enter a number.")

if __name__ == "__main__":
    main()
