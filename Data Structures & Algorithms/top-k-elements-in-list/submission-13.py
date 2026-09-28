class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        buckets = [[] for x in range(max(dic.values()) + 1)]
        for val in dic:
            buckets[dic[val]].append(val)
        
        res = []
        for i in range(len(buckets) -1, 0, -1):
           for val in buckets[i]:
            res.append(val)
            print(res)
            if len(res) == k:
                return res
        
            


