class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        
        while True:
            fast = nums[fast]
            fast = nums[fast]
            
            slow = nums[slow]
            
            if slow == fast:
                slow = 0
                break
        
        while True:
            fast = nums[fast]
            slow = nums[slow]
            
            if slow == fast:
                return slow
            
        return -1
