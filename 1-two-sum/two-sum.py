class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complements = {}

        for n, value in enumerate(nums):
            complement = target - value
            if value in complements:
                return [complements[value], n]
            complements[complement] = n
