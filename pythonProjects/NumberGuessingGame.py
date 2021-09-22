import random

print("Please make all inputs as integers. Non-integer inputs will be rejected.")
min = int(input("Enter minimum range: "))
max = int(input("Enter maximum range: "))
number = random.randint(min, max)

guess = input("Enter your first guess: ")
print(str(min) + str(max) + str(number) + str(guess))