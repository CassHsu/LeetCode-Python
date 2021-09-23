class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            if op == "--X" or op == "X--":
                ans -= 1
            if op == "++X" or op == "X++":
                ans += 1
                
        return ans
