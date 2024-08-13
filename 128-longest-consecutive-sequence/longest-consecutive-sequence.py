class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numBank = set(nums)
        max_count = 0
        
        for n in nums:
            count = 0
            if (n-1) not in numBank:
                count += 1
                while (n+1) in numBank:
                    n += 1
                    count += 1
            max_count = max(max_count, count)

        return max_count
 
