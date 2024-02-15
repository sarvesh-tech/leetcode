class Solution:
    def maxArea(self, height: List[int]) -> int:
        # length = right - left
        # min(left, right) squared * length

        #check which one higher, left or right
        #if right higher, increment left
        #if left higher, decrement right

        left = 0 
        right = len(height)-1

        maxArea = 0

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, area)

            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
        return maxArea

        




