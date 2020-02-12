x = [0, 0, 0, 1, 0, 0]

# x = [0, 0, 1, 0, 0, 1, 0]

index = 0
count = 0

while True:

    if index < len(x) - 2:
        if x[index + 2] != 1:
            index += 2
        else:
            index = index + 1
        count += 1

    elif index < len(x) - 1:
        index += 1
        count+=1
    else:
        break
