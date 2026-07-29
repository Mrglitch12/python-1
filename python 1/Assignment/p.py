def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").strip().upper()

    if choice == "C":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    elif choice == "F":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
    else:
        print("Invalid choice. Please enter C or F.")

main()