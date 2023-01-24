class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [False] * n
        trusted = [0] * n

        for t in trust:
            trusts[t[0] - 1] = True
            trusted[t[1] - 1] += 1

        judge = []
        for i, t in enumerate(trusts):
            if t == False:
                judge.append(i)

        if len(judge) != 1:
            return -1

        return judge[0] + 1 if trusted[judge[0]] == n - 1 else -1
