import json
import os

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

def messages(message):
    return MESSAGES[LANGUAGE][message]

def prompt(key):
    message = messages(key)
    print(f'=> {message}')

def get_number(key):
    prompt(key)
    number = input()

    while invalid_number(number):
        prompt(f'invalid_{key}')
        number = input()

    return float(number)

def invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True

    return False

def exit_calculator():
    prompt('new_calculation')
    answer = input()

    while not answer or answer[0].lower() not in ['y', 'n']:
        prompt('invalid_answer')
        answer = input()

    return answer[0].lower() == 'n'

os.system('clear')

prompt('welcome')

while True:
    loan_amount = get_number('loan_amount')

    apr = get_number('apr') / 100

    loan_years = get_number('loan_years')

    loan_months = loan_years * 12

    if apr:
        monthly_interest = apr / 12

        monthly_payment = loan_amount * (
            monthly_interest /
            (1 - (1 + monthly_interest) ** (-loan_months))
        )
    else:
        monthly_payment = loan_amount / loan_months

    print('---------------------------------------')
    print(f'{messages('monthly_payment')}{round(monthly_payment, 2)}')
    print('---------------------------------------')

    if exit_calculator():
        break

    os.system('clear')

prompt('thank_you')