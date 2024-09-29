def convert_temperature():
    temp = float(input("Enter temperature: "))
    unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().upper()

    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
        print(f"{temp}°C is {converted:.2f}°F.")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted = (temp - 32) * 5/9
        print(f"{temp}°F is {converted:.2f}°C.")
    else:
        print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")