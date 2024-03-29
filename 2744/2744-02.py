class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0

        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    count += 1

        return count
