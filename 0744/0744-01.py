class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters.sort()

        idx = 0
        for i, t in enumerate(letters):
            if t == target:
                idx = i

        return letters[idx + 1] if idx + 1 < len(letters) else letters[0]
