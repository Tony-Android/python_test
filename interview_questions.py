import math


def reverse_string(word):
    return ''.join(reversed(word))


def test_reverse_string():
    input_str = "TripleTen"
    reversed_str = reverse_string(input_str)
    assert reversed_str == "neTelpirT"

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)


def test_reverse_string():

    input_str = "UrbanRoutes"
    reversed_str = reverse_string(input_str)
    assert reversed_str == 'setuoRnabrU'

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)


def is_palindrome(word):
    revesed_string = ''.join(reversed(word))
    return word == revesed_string


def test_is_palindrome():

    input_str = "racecar"
    result = is_palindrome(input_str)
    assert result == True
    print("Test Passed!" + input_str + " is a palindrome")


def compute_factorial(number):
    return math.factorial(number)


def test_compute_factorial():

    input_number = 5
    result = compute_factorial(input_number)
    assert result == 120
    print("Test Passed!" + str(input_number) + " is " + str(result))
