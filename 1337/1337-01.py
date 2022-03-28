class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = []
        for i, row in enumerate(mat):
            counts.append((i, sum(row)))
            
        counts.sort(key = lambda t: t[1])
        return [c[0] for c in counts[:k]]
