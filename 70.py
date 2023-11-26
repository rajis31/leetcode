class Solution:
    def climbStairs(self, n: int) -> int:
        fibs = [1,1]
        if n == 1:
            return 1
        elif n>1:
            for i in range(2,n):
                fibs.append(fibs[i-1] + fibs[i-2])
            return fibs[n-1] + fibs[n-2]
        else:
            return 0


        
        
