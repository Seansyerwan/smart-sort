import random


def answered_question() -> bool:
    """
    This acts as the question creator for the sorting function.
    We will give a random operator as well.
    :return: If the user guessed correctly, then we return their guess equal to the answer.
    """
    num1 = random.randint(0, 10000)
    num2 = random.randint(0, 10000)
    factorial_range = random.randint(12, 25)
    res = 1
    operation = random.randint(0,6)

    match operation:
        case 0:
            res = num1 + num2
            print(f"{num1} + {num2} is what?\n")
        case 1:
            res = num1 - num2
            print(f"{num1} - {num2} is what?\n")
        case 2:
            res = num1 * num2
            print(f"{num1} * {num2} is what?\n")
        case 3:
            res = num1 // num2
            print(f"{num1} // {num2} is what?\n")
        case 4:
            for i in range(0, factorial_range):
                res *= (factorial_range - i)
            print(f"{factorial_range} factorial is what?")
            print(f"{res}")
        case _:
            res = num1 % num2
            print(f"{num1} % {num2} is what?\n")

    ans = int(input("Please input your answer: ")) # swapped to int for precision.

    # print(f"{ans} : ans\n{res} : res") debugging code...
    return res == ans
