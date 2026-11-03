class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        max_p=nums[0]
        min_p=nums[0]
        res=nums[0]
        for i in range(1,n):
            if nums[i]<0:
                max_p,min_p=min_p,max_p
            max_p=max(nums[i],nums[i]*max_p)
            min_p=min(nums[i],nums[i]*min_p)
            res=max(res,max_p,min_p)
        return res


        