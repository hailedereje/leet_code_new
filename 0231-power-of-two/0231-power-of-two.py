class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 2
        if n == 1:
            return True
        def power(x,n):
            
            if n/x == 1:
                return True
            elif(n/x < 1):
                return False
            n = n/x
            return power(x,n)
        return power(x,n)
        