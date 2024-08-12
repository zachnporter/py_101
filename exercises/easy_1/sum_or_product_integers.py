# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product of
# all numbers between 1 and the entered integer, inclusive.

# Examples:
'''
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.

Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
'''

import os

def get_integer():
    number = input('Please enter an integer greater than 0: ')

    while not valid_number(number):
        number = input('Invalid input. '
                       'Please enter an integer greater than 0: ')

    return int(number)

def get_operation():
    operation = input('Enter "s" to compute the sum, '
                      'or "p" to compute the product: ')

    while not operation or operation[0].lower() not in ['s', 'p']:
        operation = input('Invalid input. Enter "s" to compute the sum, '
                         'or "p" to compute the product: ')

    return operation[0].lower()

def valid_number(num):
    try:
        int(num)
    except ValueError:
        return False

    return int(num) > 0

def calculate_sum(number):
    return sum(list(range(1, number + 1)))

def calculate_product(number):
    product = 1

    for num in range(1, number + 1):
        product *= num

    return product

def print_result(number, operation):
    if operation == 's':
        print('The sum of integers '
              f'between 1 and {number} is {calculate_sum(number)}')
    elif operation == 'p':
        print('The product of integers '
              f'between 1 and {number} is {calculate_product(number)}')

def run_program():
    os.system('clear')

    integer = get_integer()
    operation = get_operation()

    print_result(integer, operation)

run_program()
