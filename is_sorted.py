def is_array_sorted(arr):
    for i in range(0,len(arr)):
        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                return False

    return True