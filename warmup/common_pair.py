# def common_pair(n, ar):
#     if n>100:
#         return 0
#
#     pass
#
#
# n = 9
x = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#
#
# x.sort()
# #
# final_list = []
# temp = []
# for i in range(len(x)):
#     # if len(x)>i+1:
#         if x[i]+1 in x :
#             temp.append(x[i])
#         else:
#             if len(temp)>1:
#                 temp.append(x[i])
#                 final_list.append(temp)
#             temp = []



def sockMerchant(n, ar):
    if 101 < n < 0:
        return 0
    count = 0
    while True:
        element = ar.pop()

        if element in ar:
            count+=1
            ar.remove(element)
        if len(ar)==0:
            return count
    #
    # for i in ar:
    #     ar.remove(i)
    #     if i in ar:
    #         ar.remove(i)
    #         count += 1
    # return count


# ar = [10, 30, 10]
ar = [6 ,5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 3
print(sockMerchant(n , ar))