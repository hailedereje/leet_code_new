class Solution:
    
    def findTheWinner(self, n: int, k: int) -> int:
        def finder(n,k):
            if n == 1:
                return 0
            prev = finder(n-1,k)
            return (prev+k) % n
        
        return finder(n,k)+1
        
        
            

    
                
            
            
            
            
            
        
        