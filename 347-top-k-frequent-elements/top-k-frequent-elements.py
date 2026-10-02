import collections
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = collections.Counter(nums)
        return [num for num, frequency in count.most_common(k)]