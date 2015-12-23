try:
    count = int(input("Give me a number: "))
except ValueError:
    print("Thats not a number!")
else:
    print("Hi" * count)