# bubble sort
x = [1, 5, 2, 4, 8, 6, 11, 3]


def bubble_sort(x):
    for j in range(len(x)):
        for i in range(len(x) - 1 - j):
            if x[i] > x[i + 1]:
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp


x = [1, 2, 3, 4, 5, 6, 8, 11]
target = 11



def binary_search(x, target):
    low = 0
    high = len(x) - 1
    while low <= high:
        mid = (low+high) // 2
        if x[mid] == target:
            return "FOUND"
        elif x[mid] > target:
            high = mid-1
        elif x[mid] < target:
            low = mid+1
    return "not found"



def binary_search_recursive(x, target, low, high):
    print("low: ",low)
    print("high: ", high)
    if low >= high:
        return "not found"
    else:
        mid = (low+high)//2
        if x[mid] == target:
            return "Found"
        elif x[mid] > target:
            return binary_search_recursive(x, target, low, mid-1)
        elif x[mid] < target:
            return binary_search_recursive(x, target, mid+1, high)





y = binary_search_recursive(x, target=13, low=0, high=len(x))
