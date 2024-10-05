import random


def answered_question() -> bool:
    """
    This acts as the question creator for the sorting function.
    We will give a random operator as well.
    :return: If the user guessed correctly, then we return their guess equal to the answer.
    """

    # all of our variables below are here
    num1 = random.randint(0, 10000)
    num2 = random.randint(0, 10000)
    factorial_range = random.randint(12, 40)
    exponent_range = random.randint(-99, 99)
    res = 1
    operation = random.randint(0,6)

    # we match what the operation is with this statement
    match operation:
        case 0: # addition
            res = num1 + num2
            print(f"{num1} + {num2} is what?\n")
        case 1: # subtraction
            res = num1 - num2
            print(f"{num1} - {num2} is what?\n")
        case 2: # multiplication
            res = num1 * num2
            print(f"{num1} * {num2} is what?\n")
        case 3: # division with no remainders
            res = num1 // num2
            print(f"{num1} // {num2} is what?\n")
        case 4: # finding the factorial number
            for i in range(0, factorial_range):
                res *= (factorial_range - i)
            print(f"{factorial_range} factorial is what?")
            print(f"{res}")
        case 5: # raising a number to the power of another
            res = pow(num1, exponent_range)
            print(f"{num1} to the power of {exponent_range} is what?") # this results in stupidly large numbers
        case _:
            res = num1 % num2 # get the modulo
            print(f"{num1} % {num2} is what?\n")

    ans = int(input("Please input your answer: ")) # swapped to int for precision.

    # print(f"{ans} : ans\n{res} : res") debugging code...
    return res == ans
