class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n_str = ''
        for n in num:
            n_str += str(n)
         
        return [int(n) for n in str(int(n_str) + k)]
