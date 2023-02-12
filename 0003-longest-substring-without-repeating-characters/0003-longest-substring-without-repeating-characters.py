class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <=1:
            return len(s)
        maxs = 0
        for p1 in range(len(s)):
            arrays = []
            for p2 in range(p1,len(s)):
                if s[p2] not in arrays:
                    arrays.append(s[p2])
                    maxs = max(maxs,len(arrays))
                else:
                    break
        return maxs    