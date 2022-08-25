money_invested = eval(input("Enter the amount you want to invest: "))
interest_rate = eval(input("Enter the interest rate: "))

money_invested = float(money_invested)
interest_rate = float(interest_rate)

for i in range(0, 9):
    Earnings = money_invested + (money_invested * interest_rate)
    print("{:.2f}". format(Earnings))