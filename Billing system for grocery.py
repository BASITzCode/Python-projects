# Task = calculate bill
def calculate_bill(*kwargs):
    total = sum(args)
    return total
try:
    n_items = int(input("Enter the number of items you bought: "))
except:
    raise ValueError("Please enter a valid number")
prices = []
#List to store the prices of the items
for i in range(n_items):
    item_price = float(input(f"Enter the price of item {i+1} in $: "))
    prices.append(item_price)

total = calculate_bill(*prices)
if total > 100:
    print("-"*30)
    print(f'Gross total = {total}')
    total *= 0.8
    print("-"*30)
    print("You have a 20% discount!")
elif total > 50:
    print("-"*30)
    print(f'Gross total = {total}')
    total *= 0.9
    print("You have a 10% discount!")
else:
    print("You have no discount")    
print("="*30)
print(f"The total bill is: $ {total:.2f}")
print("="*30)
