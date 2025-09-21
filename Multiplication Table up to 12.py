# Program to print a multiplication table

# Ask the user for a number
number = int(input("Hey! Give me a number and I'll show its multiplication table: "))

# Print the multiplication table up to 12
print(f"\nHere is the multiplication table for {number}:")

for i in range(1, 13):
    print(number, "x", i, "=", number * i)
