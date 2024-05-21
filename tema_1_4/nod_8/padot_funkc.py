
def print_prices(prices):
    for food, price in prices.item():
        print(f"prece ir {food} is {price}")

print_prices(prices, threshold=1.0)

