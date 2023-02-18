class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        count = 0
        start,end = 0,1
        
        while(end < len(nums)):
            if nums[start] == nums[end]:
                nums.pop(end)
                count+=1
            else:
                start+=1
                end+=1
        return len(nums)
            
                
                
        