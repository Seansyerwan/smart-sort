import random


def answered_question() -> bool:
    """
    This acts as the question creator for the sorting function.
    We will give a random operator as well.
    :return: If the user guessed correctly, then we return their guess equal to the answer.
    """
    num1 = random.randint(0,1000)
    num2 = random.randint(0,1000)
    res = 0
    operation = random.randint(0,4)

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
        case _:
            res = num1 % num2
            print(f"{num1} % {num2} is what?\n")

    ans = float(input("Please input your answer: "))

    return res == ans