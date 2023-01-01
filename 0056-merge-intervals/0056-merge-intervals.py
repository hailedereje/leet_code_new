class Solution:
    
    def merge(self,nums: list[list[int]]):
        merged = []
        nums.sort(key= lambda i:i[0])
        merged = [nums[0]]
        for start ,end in nums:
            if merged[-1][1] >= start:
                merged[-1][1] = max(end,merged[-1][1])
            else:
                merged.append([start,end])

        print(merged)
        return merged
        