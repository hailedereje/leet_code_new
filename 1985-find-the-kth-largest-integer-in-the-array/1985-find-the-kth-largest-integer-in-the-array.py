class Solution:
    def kthLargestNumber(self,nums: list[str], k: int) -> str:
        nums.sort(key= lambda i:-int(i))
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        print(nums[k-1])
        return str(nums.pop(k-1))
        