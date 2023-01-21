class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 3
        if n == 1:
            return True
        def power(x,n):
            summ = n/x
            n = summ
            if summ == 1:
                return True
            elif(summ < 1):
                return False
            
            return power(x,n)
        return power(x,n)
        