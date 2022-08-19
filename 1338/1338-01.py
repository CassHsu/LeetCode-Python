class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)

        counts = [c for _, c in counts.most_common()]

        removed = 0
        size = 0

        for c in counts:
            removed += c
            size += 1
            if (removed >= len(arr) // 2):
                break

        return size
