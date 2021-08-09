class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tmp = ""
        for i in s:
            tmp += str(ord(i) - 96)
        
        for _ in range(k):
            tmp = str(sum([int(i) for i in tmp]))
            
        return int(tmp)
