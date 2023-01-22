class Solution(object):
    def solve(self,dp,nums,player,start,end):
        if(start>end):
            return 0
        if(dp[start][end][player]!=-1):
            return dp[start][end][player]
        if(player==0):
            dp[start][end][player]=max(nums[start]+self.solve(dp,nums,1,start+1,end),nums[end]+self.solve(dp,nums,1,start,end-1))
            return dp[start][end][player]
        else:
            dp[start][end][player]=min(-nums[start]+self.solve(dp,nums,0,start+1,end),-nums[end]+self.solve(dp,nums,0,start,end-1))
            return dp[start][end][player]

    def PredictTheWinner(self,nums):
        dp=[[[-1 for i in range(2)] for i in range(len(nums))] for i in range(len(nums))]
        ans=self.solve(dp,nums,0,0,len(nums)-1)
        if(ans>=0):
            return True
        else:
            return False