class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            code = [0] * 26
            for c in word:
                code[ord(c) - ord("a")] += 1
            
            anagrams[tuple(code)].append(word)
        
        return(list(anagrams.values()))

        