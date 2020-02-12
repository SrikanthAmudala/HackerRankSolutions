s = "UDDDUDUU"

s = "DDUUUUDD"

s = "udddududuuduu"



count = 0
vally_count = 0
mount_valley_list = []
flag = False
for i in s:
    count_prev = count
    if i.upper() == "U":
        count += 1
    elif i.upper() == "D":
        count += -1

    if count_prev == -1 and count == 0:
        flag = True

    if flag == True:
        vally_count += 1
        flag = False


c = [0,1,0,0,0,1,0]