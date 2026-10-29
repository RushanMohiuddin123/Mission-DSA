class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total=sum(nums)
        if total %2 !=0:
            return False
        target=total//2
        n=len(nums)
        # memo={}
        # def f(i,target):
        #     if target==0:
        #         return True
        #     if i>=n or target<0:
        #         return False
        #     if (i,target) in memo:
        #         return memo[(i,target)]
        #     take=f(i+1,target-nums[i])
        #     skip=f(i+1,target)
        #     memo[(i,target)]=take or skip
        #     return memo[(i,target)]
        # return f(0,target)

# Bottom Up
        dp=[False]*(target +1)
        dp[0]=True
        for x in nums:
            for y in range (target,0,-1):
                if y>=x:
                    dp[y]=dp[y] or dp[y-x]
        return dp[target]
        