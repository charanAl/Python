# Second Largest Number Without Sorting

def second_largest_num(arr):
    first = sencond = float('inf')
    for num in arr:
        if num> first:
            sencond = first
            first = num
        elif num > sencond and num != first:
            sencond =  num
    return sencond
