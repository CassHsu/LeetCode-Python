class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0
            
            for n in nums:
                if current_sum + n <= max_sum_allowed:
                    current_sum += n
                else:
                    current_sum = n
                    splits_required += 1

            return splits_required + 1
        
        minimum_largest_split_sum = 0
        left = max(nums)
        right = sum(nums)
        while left <= right:
            max_sum_allowed = (left + right) // 2
            
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                left = max_sum_allowed + 1
        
        return minimum_largest_split_sum
