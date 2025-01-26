# celsius to fahrenheit

celsius_value = float(input("Enter your value = "))
def celsius_to_fahrenheit(celsius):
    fah = (celsius * 9/5) + 32
    print(f"Your result in fahrenheit is = {fah}")

celsius_to_fahrenheit(celsius_value)