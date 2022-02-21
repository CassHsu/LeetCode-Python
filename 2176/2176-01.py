class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        m = {}
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[i] == nums[j] and (i, j) not in m:
                        if (i * j) % k == 0:
                            m[(i, j)] = True
                            m[(j, i)] = True
                            count += 1
        return count
