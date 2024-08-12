# Build a program that asks the user to enter the
# length and width of a room, in meters,
# then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet).
# Compute the area accordingly and print it and its conversion in parentheses.

def get_unit_of_measurement():
    print('Would you like to compute the area in (m)eters or (f)eet?')
    unit_of_measurement = input().lower()

    while not valid_selection(unit_of_measurement):
        print('Please make a valid selection: (m)eters or (f)eet:')
        unit_of_measurement = input().lower()

    if unit_of_measurement[0] == 'm':
        return 'meters'
    else:
        return 'feet'

def valid_selection(input):
    return input and input[0] in ['m', 'f']

def get_measurement(measure, unit):
    print(f'Enter the {measure} of the room in {unit}:')
    measurement = input()

    while not valid_measurement(measurement):
        print('Enter a valid number greater than zero:')
        measurement = input()

    return float(measurement)

def valid_measurement(measurement):
    try:
        float(measurement)
    except ValueError:
        return False
    
    return float(measurement) > 0

def calculate_area(length, width, unit):
    if unit == 'meters':
        sq_meters = length * width
        sq_feet = sq_meters * 10.7639
    else:
        sq_feet = length * width
        sq_meters = sq_feet / 10.7639

    return sq_meters, sq_feet

def print_result(sq_meters, sq_feet, unit):
    if unit == 'meters':
        print(f'The area of the room is {sq_meters:.2f} square meters ({sq_feet:.2f} square feet).')
    else:
        print(f'The area of the room is {sq_feet:.2f} square feet ({sq_meters:.2f} square meters).')


def run_program():
    unit_of_measurement = get_unit_of_measurement()

    length = get_measurement('length', unit_of_measurement)
    width = get_measurement('width', unit_of_measurement)

    sq_meters, sq_feet = calculate_area(length, width, unit_of_measurement)

    print_result(sq_meters, sq_feet, unit_of_measurement)

run_program()