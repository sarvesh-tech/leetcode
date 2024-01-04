class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1,2,3,0,0,0]


        # left = 0 
        # right = 0

        # while nums1[left] > nums2[right]:
        #     left += 1
        
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        
        nums1.sort()
        
        