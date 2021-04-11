from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wset = set(wordDict)
        q = deque()
        visited = set()
        
        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wset:
                    q.append(end)
                    if end == len(s):
                        return True
                visited.add(start)
        return False
