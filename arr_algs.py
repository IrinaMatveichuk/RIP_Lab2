def findmin(arr):
    min_el = arr[0]
    for el in arr:
        if el < min_el:
            min_el = el
    return min_el


def arifaverage(arr):
    sum_al = 0
    for el in arr:
        sum_al = sum_al + el
    sum_al = sum_al/len(arr)
    return sum_al

arr = [10, 2, 3, 8]
print(findmin(arr))
print(arifaverage(arr))
