import random



"""
This is a joke sorting algorithm, smart sort. We will assume you are smart enough to solve mathematic questions
So, we will put in an array. we will assume the user is capable of answering the questions should it be good. 
"""
def sort(array):

    while(True):
        repeat = False #track if we repeat

        #we do a mock sorting algorithm like bubble sort
        for i in range(0,len(array)-1):
            for j in range (0, len(array)-i-1):
                if array[j] > array[j+1]: #should there be a discrepancy, swap
                    if not answered_question(): #if they answer falsely
                        random.shuffle(array) #reshuffle
                        print("Answer incorrect, scrambling array. Work on your math!\n")
                        repeat = True
                        break
                    else:
                        temp = array[j]
                        array[j]= array[j+1]
                        array[j+1] = temp

        if repeat:
            continue
        else:
            print("sorting complete.")
            break




def answered_question() -> bool:
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)

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



arr = [2,1,4]
sort(arr)

for i in range(0,len(arr)):
    print(f"{arr[i]} ")

