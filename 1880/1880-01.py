class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_num = int("".join([str(ord(c) - ord('a')) for c in firstWord]))
        second_num = int("".join([str(ord(c) - ord('a')) for c in secondWord]))
        target_num = int("".join([str(ord(c) - ord('a')) for c in targetWord]))
        
        return first_num + second_num == target_num
