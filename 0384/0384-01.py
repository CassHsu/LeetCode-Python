class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.origin = list(nums)

    def reset(self) -> List[int]:
        self.array = self.origin
        self.origin = list(self.origin)
        return self.array
        

    def shuffle(self) -> List[int]:
        arr = list(self.array)
        
        for i in range(len(self.array)):
            remove_i = random.randrange(len(arr))
            self.array[i] = arr.pop(remove_i)
            
        return self.array
