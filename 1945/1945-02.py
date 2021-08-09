class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tmp = "".join([str(ord(c) - 96) for c in s])
        
        for _ in range(k):
            tmp = str(sum([int(i) for i in tmp]))
            
        return int(tmp)
