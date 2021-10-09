class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [] if n*m != len(original) else [original[i*n:(i+1)*n] for i in range(m)]
