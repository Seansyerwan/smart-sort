import random

wordList = []  # word list for the rest of the code


def word_add():
    """
    Function to fill in the words from the dictionary file
    :return: Not applicable
    """
    with open("dictionary.txt", 'r') as word_file:
        for word in word_file:
            word = word.strip().lower()  # strips of any whitespace.

            wordList.append(word)  # add the word to the list.


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
    values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
              'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    word_add()
    word_num = random.randint(0, len(wordList))
    operation = random.randint(0, 9)

    # we match what the operation is with this statement
    match operation:
        case 0:  # addition
            res = num1 + num2
            print(f"{num1} + {num2} is what?\n")
        case 1:  # subtraction
            res = num1 - num2
            print(f"{num1} - {num2} is what?\n")
        case 2:  # multiplication
            res = num1 * num2
            print(f"{num1} * {num2} is what?\n")
        case 3:  # division with no remainders
            res = num1 // num2
            print(f"{num1} // {num2} is what?\n")
        case 4:  # finding the factorial number
            for i in range(0, factorial_range):
                res *= (factorial_range - i)
            print(f"{factorial_range} factorial is what?")
            print(f"{res}")
        case 5:  # raising a number to the power of another
            res = pow(num1, exponent_range)
            print(f"{num1} to the power of {exponent_range} is what?")  # this results in stupidly large numbers
        case 6:  # square root
            res = num1 ** (1 / 2)
            print(f"The square root of {num1} is what?")
        case 7:  # cubic root
            res = num1 ** (1 / 3)
            print(f"The cubic root of {num1} is what?")
        case 8:
            res = num1 % num2  # get the modulo
            print(f"{num1} % {num2} is what?\n")
        case _:
            res = 0  # set it to 0 just to be careful
            for i in range(0, len(wordList[word_num])):
                res += values[wordList[word_num][i]]
            print(f"The word is {wordList[word_num]}, what is the scrabble value?")

    ans = int(input("Please input your answer: "))  # swapped to int for precision.

    # print(f"{ans} : ans\n{res} : res") debugging code...
    return res == ans
