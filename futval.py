print("Hello, thank you for choosing Gold bank; we would like to know your name")
name = input("What is your name? ")
principal = eval(input("{} how much do you want to invest? ".format(name)))
apr = eval(input("Enter the annual interest rate: "))
time = eval(input("How many years would you like to make this investment? "))
print(name, "you want to deposit an amount of", principal, "at the annual interest rate of", apr, "% for", time, "years")

for i in range(time):
    principal = principal * (1 + apr)

print("The value in {} years is: ".format(time), principal, "naira")