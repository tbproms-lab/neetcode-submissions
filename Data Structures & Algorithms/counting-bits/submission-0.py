class Solution:
    def countBits(self, n: int) -> List[int]:
        lyst = []
        for x in range(n+1):
            res = 0
            while(x):
                x &= x -1
                res += 1
            lyst.append(res)
        
        return lyst
            
