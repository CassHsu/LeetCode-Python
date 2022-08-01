class NumArray:
    nums = []
    total = 0

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.total = sum(nums)

    def update(self, index: int, val: int) -> None:
        v = self.nums[index]
        self.nums[index] = val
        self.total = self.total - v + val

    def sumRange(self, left: int, right: int) -> int:
        sum_left = sum(self.nums[0: left])
        sum_right = sum(self.nums[right + 1:])
        return self.total - sum_left - sum_right
