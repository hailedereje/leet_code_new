class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:        
        def f(self, nums, start, end, person, scores) -> bool :
            if start > end :
                return scores [ 0 ] >= scores [ 1 ]             
            
            scores [ person ] += nums [ start ]
            case1  = f(self, nums, start+1, end,( person+1 )%2, scores )
            scores [ person ] -= nums [ start ]
            
            if person is 0 and case1 is True :
                return True
            
            if person is 1 and case1 is False :
                return False
            
            scores [ person ] += nums [ end ]
            case2  = f(self, nums, start, end-1 ,( person+1 )%2, scores )
            scores [ person ] -= nums [ end ]  
            
            return case2
        
        scores = [0, 0]
        return f(self, nums, 0, len(nums)-1, 0, scores)