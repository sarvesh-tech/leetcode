class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #create a hasmap key:value is num:index

        #return index pair that add up to the target value

        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [i, seen[complement]]
            
            seen[nums[i]] = i 

            
