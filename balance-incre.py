# 5% balance increament

balance = int(input("Enter the initial balance: "))
months = int(input("Enter the months: "))

for month in range(1, months +1):
    balance *= 1.05
    print(f"month= {month}:{balance}")

