class Solution:
    def moveZeroes(self, nums: list) -> None:
        val = 0
        n = len(nums)
        while(val < n):
            if nums[val] == 0:
                nums.append(nums.pop(val))
                n-=1
            else:
                val+=1
        
        return nums
        