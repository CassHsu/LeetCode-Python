class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = []
        counts = []
        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                if nums[i] not in targets:
                    targets.append(nums[i])
                    counts.append(0)
        
        for t, target in enumerate(targets):
            for i in range(1, len(nums)):
                if nums[i - 1] == key and nums[i] == target:
                    counts[t] += 1
        
        imax = 0
        mx = 0
        for i, c in enumerate(counts):
            if c > mx:
                mx, imax = c, i
        
        return targets[imax]
