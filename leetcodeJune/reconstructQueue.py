def reconstructQueue(people):
    # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    people.sort(reverse=True)
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            if people[i][0] == people[j][0]:
                if people[i][1] > people[j][1]:
                    temp = people[i][1]
                    people[i][1] = people[j][1]
                    people[j][1] = temp
            else:
                break

    temp = []
    for i in range(len(people)):
        temp.insert(people[i][-1], people[i])
    return temp

people = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]