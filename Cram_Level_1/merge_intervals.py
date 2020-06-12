x = [[1, 3], [2, 6], [8, 10], [15, 18]]

x.sort()
temp = []

for i in range(0, len(x) - 1):
    if x[i][-1] > x[i + 1][0]:
        temp.append([x[i][0], x[i + 1][-1]])
    else:
        temp.append(x[i])
i = 0

x = [[1, 3], [2, 6], [8, 10], [15, 18]]

x = [[1, 4], [4, 5]]

temp = []

while i < len(x) - 1:
    flag = 0
    if x[i][-1] >= x[i + 1][0] and x[i][0] <= x[i+1][0] :
        temp.append([x[i][0], min(x[i][-1], x[i + 1][-1])])
        i += 2
    else:
        temp.append(x[i])
        i += 1
        flag = 1
    if i == len(x) - 1 and flag == 1:
        temp.append(x[i])
