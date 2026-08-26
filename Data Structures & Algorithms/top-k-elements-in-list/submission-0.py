class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        #putting eles into freq and bucket
        for n,count in freq.items():
            bucket[count].append(n)
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                result.append(n)
            if len(result)==k:
                return result
        