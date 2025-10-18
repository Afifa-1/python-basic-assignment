# Two number relationship

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

if num1 > num2:
    print("First num is greater than second")
elif num1 == num2:
    print("Both numbers are equal")
else:
    print("Second number is greater the first")


if num1 % 2 == 0 and num2 % 2 == 0 :
    print("Both are even")

elif num1 % 2 != 0 and num2 % 2 != 0 :
    print("Both are odd")
else:
    print("Both are mixed")