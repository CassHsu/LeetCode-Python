from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)

        m = defaultdict(list)
        for w in wordList:
            for i in range(L):
                m[w[:i] + "*" + w[i+1:]].append(w)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            curr, level = queue.popleft()
            for i in range(L):
                w = curr[:i] + "*" + curr[i+1:]

                for word in m[w]:
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                m[w] = []
        return 0
