temp = int(input("Enter a number: "))
if temp < 0:
    print("It's freezing")
elif 0<= temp < 15:
    print("It's cool outside!")
elif 15<= temp < 25:
    print("It's warm outside!")
else:
    print("It's hot outside!")
