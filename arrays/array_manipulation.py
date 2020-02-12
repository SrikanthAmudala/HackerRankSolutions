q = [
    [1, 2, 100],
    [2, 5,100],
    [3, 4, 1]
]

n = 5

final_list = [0]*n
for i in q:
    for j in range(i[0]-1, i[1]):
        final_list[j]+=i[-1]

