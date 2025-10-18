# bill counter

a = int(input("Enter the the total  amount of bill: "))

stars = ""

for digit in str(a):
    stars += "*"
print("total bill count is:", stars)