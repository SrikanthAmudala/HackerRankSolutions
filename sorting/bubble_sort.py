x = [9, 5, 6, 2, 3, 1, 6, 4, 9, 10]


def bubble_sort(x):
    while True:
        swapped = False
        for i in range(0, len(x) - 1):
            if x[i] > x[i + 1]:
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp
                swapped = True
        if swapped == False:
            break
    return x


# 4 3 1 2

# 2 3 1 4

# 1 3 2 4

# 1 2 3 4

arr = [[7, 6, 8, 2, 4, 3],
       [7, 3, 3, 0, 6, 1],
       [3, 8, 7, 7, 2, 2],
       [0, 8, 6, 8, 6, 1],
       [7, 1, 6, 0, 2, 4],
       [2, 7, 8, 1, 7, 4]]



i = 0
hour_glass = [arr[i][i], arr[i][i + 1], arr[i][i + 2],
              arr[i + 1][i], arr[i + 1][i + 1], arr[i + 1][i + 2],
              arr[i + 2][i], arr[i + 2][i + 1], arr[i + 2][i + 2]]
max_hour_glass = sum(hour_glass)
for j in range(0, len(arr) - 2):
    for i in range(len(arr) - 2):
        hour_glass = [arr[j][i], arr[j][i + 1], arr[j][i + 2],
                      arr[j + 1][i + 1],
                      arr[j + 2][i], arr[j + 2][i + 1], arr[j + 2][i + 2]]
        if sum(hour_glass) > max_hour_glass:
            max_hour_glass = sum(hour_glass)
