class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []

        L = 0
        R = n

        for i in range(0, n):
            arr.append(nums[L])
            arr.append(nums[R])
            L+=1
            R+=1
        
        return arr


