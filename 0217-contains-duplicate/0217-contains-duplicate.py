class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for i in range(len(nums)):
            if nums[i] in sett:
                return True
            sett.add(nums[i])
        return False