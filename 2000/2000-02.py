class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        l, r = 0, idx
        arr = [w for i, w in enumerate(word) if i <= idx]
        
        while l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
        return "".join(arr) + word[idx+1:]
