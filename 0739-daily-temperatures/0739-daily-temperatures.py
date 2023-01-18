class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, ans = [], [0]*len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i-cur
            stack.append(i)
        
        return ans 