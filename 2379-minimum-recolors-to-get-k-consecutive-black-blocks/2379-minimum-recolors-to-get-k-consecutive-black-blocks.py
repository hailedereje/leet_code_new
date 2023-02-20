class Solution:
    def minimumRecolors(self, nums: str, k: int) -> int:
        s,e = 0,k-1
        start = 0
        count =val = 0
        
        for i in range(len(nums)):
            print(val)
            if nums[i] == "B":
                val+=1
                
            if i - start + 1 == k:
                count = max(count,val)
                if nums[start] == "B":
                    val-=1
                
                start+=1
                     
        return k-count

        