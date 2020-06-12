def max_sub_array(nums):
    # o(n^2)
    big = min(nums)

    for j in range(len(nums)):
        temp = []
        sum_term = 0
        for i in range(j, len(nums)):
            sum_term += nums[i]
            temp.append(sum_term)
        local_big = max(temp)
        if local_big > big:
            # final_index_list = ((j, j + temp.index(local_big), local_big))
            big = local_big
    return big



def max_sub_array_time(x):
    """
    O(n)
    """
    max_value = x[0]
    big = x[0]

    for i in x[1:]:
        max_value = max(i, max_value + i)
        if max_value > big:
            big = max_value


x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]