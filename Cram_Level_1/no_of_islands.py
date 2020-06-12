x = [[0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0]]


grid = [["1","0","1","1","0","1","1"]]
gird = [["0","1","0"],["1","0","1"],["0","1","0"]]
x = []
for i in grid:
    temp = []
    for j in i:
        temp.append(int(j))
    x.append(temp)

def no_of_islands(x):
    island_count = 0
    while True:
        temp = []
        flag = 0
        for i in range(len(x)):

            for j in range(len(x[i])):
                if x[i][j] != 0:
                    if i+1 < len(x):
                        if x[i + 1][j] != 0:
                            temp.append([i, j])
                            temp.append([i + 1, j])
                        else:
                            temp.append([i, j])
                            break
                    else:
                        temp.append([i, j])
                        # break
                else:
                    break
            # if flag==1:
            #     break

        for i in temp:
            x[i[0]][i[-1]] = 0

        if len(temp)>0:
            island_count += 1

        sum1 = 0
        for i in x:
            for j in i:
                sum1 += j
        if sum1 == 0:
            return island_count
        horizonal = 0
        vertical = len(x)


        # vertical delete
        while True:
            row_sum = 0
            for j in range(vertical):
                row_sum += x[j][horizonal]
            if row_sum == 0:
                for j in range(vertical):
                    del x[j][horizonal]
            else:
                break


        # horizonal delete
        vertical = 0
        while True:
            hor_sum = 0
            for i in range(len(x[0])):
                hor_sum += x[vertical][i]

            if hor_sum == 0:
                del x[vertical]
            else:
                break

