input1 = int(input("Enter the temprature of city A: "))
input2 = int(input("Enter the temprature of city B: "))

if input1 < input2:
    print("City B iss hotter than city A")

elif input1 > input2:
    print("City A iss hotter than city B")

else:
    print("Both cities have equal temp")