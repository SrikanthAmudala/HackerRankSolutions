
w = [3, 14, 1, 7]
lastTime = 0
temp= []
for i in w:
	print(lastTime, lastTime+i)
    temp.append([lastTime, lastTime + i])
    lastTime = i

print(temp)
