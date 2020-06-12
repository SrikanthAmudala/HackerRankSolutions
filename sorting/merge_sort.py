def merge_alog(arr1, arr2):
    merged_list = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            merged_list.append(arr2[j])
            j = j + 1
        else:
            merged_list.append(arr1[i])
            i = i + 1

    for k in range(i, len(arr1)):
        merged_list.append(arr1[k])

    for k in range(j, len(arr2)):
        merged_list.append(arr2[k])
    return merged_list


def two_way_merge_sort(arr):
    temp = []
    for i in range(0, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            temp.append([arr[i + 1], arr[i]])
        else:
            temp.append([arr[i], arr[i + 1]])

    for j in range(i + 2, len(arr)):
        temp.append([arr[j]])

    j = 0
    p1 = temp[0]
    while j < len(temp) - 1:
        j = j + 1
        p1 = merge_alog(p1, temp[j])

    return p1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:])

    print(left, right)
    return merge_alog(left, right)


x = [9, 5, 6, 2, 3, 1, 6, 4, 9, 10]

# print(two_way_merge_sort(x))
print(merge_sort(arr=x))
