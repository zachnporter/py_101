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

    while not valid_number(number, key):
        prompt(f'invalid_{key}')
        number = input()

    return float(number)

def valid_number(num_str, key):
    try:
        float(num_str)
    except ValueError:
        return False

    if key == 'apr':
        return float(num_str) >= 0

    return float(num_str) > 0

def calculate_monthly_payment(loan_amount, loan_months, apr):
    if apr:
        monthly_interest = apr / 12

        monthly_payment = loan_amount * (
            monthly_interest /
            (1 - (1 + monthly_interest) ** (-loan_months))
        )
    else:
        monthly_payment = loan_amount / loan_months

    return monthly_payment

def display_monthly_payment(monthly_payment, loan_amount, loan_years, apr):
    print('---------------------------------------')
    print(f'{messages('amount')} {loan_amount:,.2f}')
    print(f'{messages('years')} {loan_years:.0f}')
    print(f'{messages('interest')} {apr * 100}%')
    print(f'{messages('monthly_payment')}{round(monthly_payment, 2)}')
    print('---------------------------------------')


def new_calculation():
    prompt('new_calculation')
    answer = input()

    while not answer or answer[0].lower() not in ['y', 'n']:
        prompt('invalid_answer')
        answer = input()

    return answer[0].lower() == 'y'

os.system('clear')

prompt('welcome')

def run_program():
    loan_amount = get_number('loan_amount')

    apr = get_number('apr') / 100

    loan_years = get_number('loan_years')

    loan_months = loan_years * 12

    monthly_payment = calculate_monthly_payment(loan_amount, loan_months, apr)

    display_monthly_payment(monthly_payment, loan_amount, loan_years, apr)

    if new_calculation():
        os.system('clear')
        run_program()

run_program()

prompt('thank_you')
