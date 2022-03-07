class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = []
        
        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                targets.append(nums[i])
        
        if len(targets) == 1:
            return targets[0]
        
        m = collections.defaultdict(int)
        for t in targets:
            m[t] += 1
        
        mx = 0
        ans = nums[0]
        for k, v in m.items():
            if v > mx:
                mx = v
                ans = k
        
        return ans
