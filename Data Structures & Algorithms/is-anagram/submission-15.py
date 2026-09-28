class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s, dic_t = Counter(s), Counter(t)
        if len(dic_s) != len(dic_t):
            return False
        
        for c in s:
            if c not in dic_t:
                return False
            dic_t[c] -= 1
            if dic_t[c] == 0:
                del dic_t[c]
        
        return sum(dic_t.values()) == 0
            
        
        