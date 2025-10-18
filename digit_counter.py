# digit counter

a = int(input("Enter the number: "))

count = 0

for digit in str(a):
    count += 1
print("total digit count is:", count)