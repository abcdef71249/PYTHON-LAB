# 6. covert tempt from celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 # formula to convert celsius to fahrenheit
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius) # calling the function
print(f"{celsius}°C is equal to {fahrenheit}°F")