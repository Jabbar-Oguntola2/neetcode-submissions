class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        output = []
        while len(output) != k:
            max_sum = 0
            max_index = ""
            for key in dic:
                val = dic[key]
                if val > max_sum:
                    max_sum = val
                    max_index = key
            
            output.append(max_index)
            del dic[max_index]
        
        return output

        