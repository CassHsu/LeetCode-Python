class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        
        def is_palindromic(w):
            i = 0
            j = len(w) - 1
            
            while i < j:
                if w[i] != w[j]:
                    return False
                i += 1
                j -= 1
                
            return True
        
        for w in words:
            if is_palindromic(w):
                ans = w
                break
        
        return ans
