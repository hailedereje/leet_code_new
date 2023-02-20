class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            return False
        hash_set = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in hash_set:
                return True
            hash_set.add(nums[r])
            if (r-l) == k:
                hash_set.remove(nums[l])
                l += 1
            
        return False