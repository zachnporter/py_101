# Write a function that computes the sum of all numbers
# between 1 and some other number, inclusive, that are
# multiples of 3 or 5. For instance, if the supplied number is 20,
# the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

def multisum(number):
    result = 0

    for num in range(1, number + 1):
        if is_multiple_of_3_or_5(num):
            result += num

    return result

def is_multiple_of_3_or_5(number):
    return number % 3 == 0 or number % 5 == 0

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
