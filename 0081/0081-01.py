class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        p = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                p = i
        
        is_little_left = len(nums[:p]) < len(nums[p:])
        n1 = nums[:p] if is_little_left else nums[p:]
        n2 = nums[p:] if is_little_left else nums[:p]
        
        if self.bin_search(n1, target):
            return True
        elif self.bin_search(n2, target):
            return True
        else:
            return False 
    
    def bin_search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        return False
