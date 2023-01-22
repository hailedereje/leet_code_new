class Solution:
    def fib(self, n: int) -> int: 
        def feb(n):
            if n > 1:
                n = feb(n-1) + feb(n-2)
            return n
        
        return feb(n)
            