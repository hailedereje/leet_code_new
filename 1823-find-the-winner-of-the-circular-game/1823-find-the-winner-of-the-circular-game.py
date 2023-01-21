class Solution:
    
    def findTheWinner(self, n: int, k: int) -> int:
        def finder(n:int, k:int)-> int:
            if(n==1):
                return 0
            prevWinner = finder(n-1, k)
            return (prevWinner + k) % n
        return finder(n,k)+1

    
                
            
            
            
            
            
        
        