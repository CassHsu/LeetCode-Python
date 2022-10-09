class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        d = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            l, h = i + 1, len(nums) - 1
            
            while(l < h):
                s = nums[i] + nums[l] + nums[h]
                
                if abs(target - s) < abs(d):
                    d = target - s
                    
                if s < target:
                    l += 1
                else:
                    h -= 1
                    
            if d == 0:
                break
                
        return target - d
