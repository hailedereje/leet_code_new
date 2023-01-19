class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        stack = [0]
        while(left < right):
            # stack.append(min(height[left],height[right]) *(right-left))
            if stack[-1] < min(height[left],height[right]) *(right-left):
                stack.append(min(height[left],height[right]) *(right-left))
            if height[left] == min(height[left],height[right]):
                left+=1
                continue
            right-=1
        return stack[-1]
            
                
            
                
                
            
            
            
        