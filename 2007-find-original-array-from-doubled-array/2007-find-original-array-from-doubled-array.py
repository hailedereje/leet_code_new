class Solution:
    
    def findOriginalArray(self,nums: list[int]) -> list[int]:
        if len(nums)%2:
            return []
        count = Counter(nums)
        nums.sort()
        ans = []
        for num in nums:
            if num ==0 and count[num]>=2:
                count[num]-=2
                ans.append(num)
            elif(count[num] and count[num*2] and num>0):
                count[num] -=1
                count[num*2] -=1
                ans.append(num)
        return ans if len(ans)== len(nums)//2 else []
                
                
            

        
        