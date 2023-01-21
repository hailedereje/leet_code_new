class Solution:
    
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(n:int, k:int)-> int:
            if(n==1):
                return 0
            prevWinner = helper(n-1, k)
            return (prevWinner + k) % n
        return helper(n,k)+1

    
                
            
            
            
            
            
        
        