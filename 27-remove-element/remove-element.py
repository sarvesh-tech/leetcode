class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #[3,3,2,2,3]

        left = 0


        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left

