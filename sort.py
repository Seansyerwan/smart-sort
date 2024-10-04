import random
from answered_question import answered_question
from is_sorted import is_sorted


def smart_sort(array):
    """
    This function is purely for the sorting of all the array. It takes in values from the user's input,
    and either sorts the array, or if at least one question is incorrect, scrambles the entire array from scratch
    :param array: Array of numbers, presumably unsorted
    :return: The sorted array
    """

    # time complexity: O(n^2 to n!), due to extensive shuffling. this is down to how good one is at maths.
    while True:
        repeat = False  # track if we repeat

        # we do a mock sorting algorithm like bubble sort
        for i in range(0, len(array) - 1):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:  # should there be a discrepancy, swap
                    if not answered_question():  # if they answer falsely
                        random.shuffle(array)  # reshuffle
                        while (True):
                            # we cover the edge case of the numbers randomly being assigned correctly.
                            # we want to punish the user. not make them happy.
                            if not is_sorted(array):
                                break
                            else:
                                random.shuffle(array)
                        print("Answer incorrect, scrambling array. Work on your math!\n")
                        repeat = True
                        break  # break out the for loop early
                    else:
                        temp = array[j]
                        array[j] = array[j + 1]
                        array[j + 1] = temp

        if repeat:  # if previously indicated we need to repeat, we do so
            continue
        else:  # otherwise end the function
            print("sorting complete.")
            break
