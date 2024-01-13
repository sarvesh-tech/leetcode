from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for c in strs:
            #add the word to the dictionary 
            dic["".join(sorted(c))].append(c)
            
        return dic.values()
        
            