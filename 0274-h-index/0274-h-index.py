class Solution:
    def hIndex(self, citations: List[int]) -> int: 
        cit = sorted(citations,reverse = True)
        count = 0
        for i ,j in enumerate(cit):
            if i < j:
                count+=1
        return count
      
                
            
        