class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end, n, max_consecutive = 0, 0, len(nums), 0
        while end < n:
            if nums[end] == 0:
                if k > 0:
                    k -= 1
                else:                  
                    max_consecutive = max(max_consecutive, end - start)
                    if nums[start] == 0:
                        k += 1
                    start += 1
                    continue
            end += 1 
        return max(max_consecutive, end - start)   