def convert_temperature():
    print("Welcome to the Temperature Conversion Program!")
    print("Enter the temperature value followed by its unit (C for Celsius, F for Fahrenheit, K for Kelvin).")
    
    # Get user inputc
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C/F/K): ").strip().upper()
    
    if unit == "C":
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f} K.")
    
    elif unit == "F":
        celsius = (temp - 32) * 5/9
        kelvin = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F is equivalent to {celsius:.2f}°C and {kelvin:.2f} K.")
    
    elif unit == "K":
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * 9/5 + 32
        print(f"{temp} K is equivalent to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
    
    else:
        print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

# Run the programs
convert_temperature()