import collections
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Calculate left products
        left_prod = 1
        for i in range(n):
            res[i] = left_prod
            left_prod *= nums[i]
            
        # Step 2: Calculate right products and multiply with left products
        right_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]
            
        return res
