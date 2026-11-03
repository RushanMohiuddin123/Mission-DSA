class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        res=nums[0]
        for i in range(0,n):
            product=1
            for j in range(i,n):
                product=product*nums[j]
                if product>res:
                    res=max(res,product)
                #     res=product
        return res

        