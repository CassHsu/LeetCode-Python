class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for h in range(len(citations), 0, -1):
            i = len(citations) - h
            if citations[i] >= h:
                return h
        return 0
