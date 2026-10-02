class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        def helper(index: int, left_prod: int) -> int:
            if index == n:
                return 1
            
            res[index] = left_prod
            right_prod = helper(index + 1, left_prod * nums[index])
            
            res[index] *= right_prod
            return right_prod * nums[index]

        helper(0, 1)
        return res