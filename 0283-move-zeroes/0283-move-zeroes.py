class Solution:
    def moveZeroes(self, nums: list) -> None:
        back = 0
        for front in range(len(nums)):
            if nums[front] != 0 and nums[back] == 0:
                nums[back], nums[front] = nums[front], nums[back]
            if nums[back] != 0:
                back += 1
        