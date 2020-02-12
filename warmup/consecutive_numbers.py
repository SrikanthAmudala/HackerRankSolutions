"""
sample output: [[1,2,3],[6,7,8]]
"""

x =[1, 2, 3, 6, 7, 8, 11, 12, 13, 15, 18, 99, 100]

def consective_numbers(x):
    x.sort()
    final_list = []
    temp = []
    for i in range(len(x)):
        # if len(x)>i+1:
        if x[i] + 1 in x:
            temp.append(x[i])
        else:
            if len(temp) > 1:
                temp.append(x[i])
                final_list.append(temp)
            temp = []
    return final_list
