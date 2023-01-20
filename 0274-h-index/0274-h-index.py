class Solution:
    def hIndex(self, citations: List[int]) -> int: 
        count = 0
        for i ,j in enumerate(sorted(citations,reverse = True)):
            if i < j:
                count+=1
        return count
      
                
            
        