import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

def messages(message):
    return MESSAGES[LANGUAGE][message]

def prompt(key):
    message = messages(key)
    print(f'=> {message}')

def get_number():
    number = input()

    while invalid_number(number):
        prompt('invalid_number')
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

prompt('welcome')

while True:
    prompt('first_number')
    number1 = get_number()

    prompt('second_number')
    number2 = get_number()

    prompt('operation')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        operation = input()

    match operation:
        case '1':
            output = number1 + number2
        case '2':
            output = number1 - number2
        case '3':
            output = number1 * number2
        case '4':
            if number2 == 0:
                prompt('division_by_zero')
                continue
            output = number1 / number2

    print(f'{messages('result')}{output}')

    if exit_calculator():
        break

prompt('thank_you')
