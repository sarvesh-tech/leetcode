class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = (2*len(nums))*[]

        ans += nums
        ans += nums

        return ans
