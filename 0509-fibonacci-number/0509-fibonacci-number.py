class Solution:
    def __init__(self):
        self.stack = [0,1]
        self.count = 0
    def fib(self, n: int) -> int: 
        if n>1:
            n = self.fib(n-1)+self.fib(n-2)
        return n
            