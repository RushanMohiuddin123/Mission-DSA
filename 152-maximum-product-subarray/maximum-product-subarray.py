class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Brute force algo
        # n=len(nums)
        # res=nums[0]
        # for i in range(0,n):
        #     product = 1
        #     for j in range(i,n):
        #         product = product * nums[j]
        #         if product > res:
        #             res = max(res,product)
        # return res


        # Using the prefix and suffix algo
        n=len(nums)
        prefix=1
        suffix=1
        res=nums[0]
        for i in range(0,n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-1-i]
            res=max(res,prefix,suffix)
        return res

        