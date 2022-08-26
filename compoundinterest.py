print("This program calculates the future value")
print("of a 10 year investment")

principal = eval(input("Enter the amount you want to invest: "))
interest_rate = eval(input("Enter the interest rate: "))

interest_rate = float(interest_rate) * .01

for i in range(10):
    principal = float(principal * (1 + interest_rate))
    #the formula can also be written as= principal+(principal*interest_rate)
    #if the print is placed here, it will print the principal value for each year, until 10
print("Investment after 10 years: {:.2f}".format(principal))