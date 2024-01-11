from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            anagram_map[''.join(sorted(word))].append(word)   
        return anagram_map.values()

                
            



            