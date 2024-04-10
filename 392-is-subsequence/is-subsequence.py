class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # have two pointers at each s and t
        # if match found while iterating t, increment s & t ptrs
        # if not found increment t, 


        n,m = len(s),len(t)
        i = j = 0

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
