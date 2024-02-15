class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = ""    
        L = 0
        R = 0

        #s = "axc", t = "ahbgdc"
        #      ^
        #                      ^

        while len(res) != len(s) and R < len(t):
            if s[L] == t[R]:
                res += t[R]
                L += 1
            R += 1
        
        return (s == res)

