# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# we check if the second number is larger than current largest_number
# and update largest_number if needed
if number2 > largest_number:
    largest_number = number2

# we check if the third number is larger than current largest_number
# and update largest_number if needed
if number3 > largest_number:
    largest_number = number3

# print the result
print("The largest number is:", largest_number)