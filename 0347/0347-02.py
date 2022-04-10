class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        kv = counter.most_common(k)
        return [k for k,v in kv]
