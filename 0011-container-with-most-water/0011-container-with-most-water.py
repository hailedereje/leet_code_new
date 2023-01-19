class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        stack = []
        while(left < right):
            stack.append(min(height[left],height[right]) *(right-left))
            if height[left] == min(height[left],height[right]):
                left+=1
                continue
            right-=1
        return max(stack)
            
                
            
                
                
            
            
            
        