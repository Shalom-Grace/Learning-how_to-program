print("Hello, user!")
print("This is a program that converts temperatures from Fahrenheit to Celsius")
fahrenheit = eval(input("Enter the temperature you would like to convert: "))
celsius = (fahrenheit-32) * 5.0/9.0
print("The temperature in Celsius is {}". format(celsius))