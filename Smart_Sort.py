import random
from sort import smart_sort


"""
This is a joke sorting algorithm, smart sort. We will assume you, the user, are smart enough to solve maths questions
So, we will put in an array. we will assume the user is capable of answering the questions should it be good. 
"""



arr = [2,1,4] # sample array
smart_sort(arr)

for i in range(0,len(arr)): # print the result
    print(f"{arr[i]} ")

