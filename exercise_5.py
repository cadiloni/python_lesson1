profit = float(input("Enter the revenue of the company "))
costs = float(input("Enter company costs"))

if profit > costs:
    print(f"The firm operates profitably. The profitability of revenue was {profit / costs:.2f}")
    workers = int(input("Enter the number of employees of the company"))
    print(f"Profit per employee was {profit / workers:.2f}")
elif profit == costs:
    print("You are not making any profits")
else:
    print("The firm is operating at a loss")
