# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

for num in range(1, 100, 2):
    print(num)

# Further Exploration

# Consider adding a way for the user to specify the
# starting and ending values of the odd numbers printed.

def print_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 1:
            print(num)

print_odd_numbers(1, 99)
