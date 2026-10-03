class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # optimize: sum_map = {} # val: index
       sum_map = {}
       for i, val in enumerate(numbers):
            complement = target - val

            if complement in sum_map:
                return [sum_map[complement]+1, i+1]
            sum_map[val] = i
                