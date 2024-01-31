class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        curr = 0
        max_total = curr
        
        for arr in accounts:
            for dollar in arr:
                curr += dollar
            if curr >= max_total:
                max_total = curr
            curr = 0
        return max_total