class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        pivot = nums[len(nums) // 2]
        moves = 0
        
        for n in nums:
            moves += abs(n - pivot)
            
        return moves
