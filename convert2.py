print("A table of Celsius temperatures and Fahrenheit equivalents:")

for celsius in (range(0, 110, 10)):
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print(celsius, fahrenheit)