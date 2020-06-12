import random
class Solution:
    
    def __init__(self, w: List[int]):
        self.w = w
        
    def pickIndex(self) -> int:
        temp = []
        lastTime = 0
        for i in self.w:
            temp.append( [lastTime, lastTime + i])
            lastTime = i
        
        
        ran = random.randint(1, temp[-1][-1])
        # print(ran)
        # print(temp)
        # [[0, 1], [1, 4], [4, 6]]
        for i in range(len(temp)):
            if ran > temp[i][0] and ran <= temp[i][-1] :
                return i
            
