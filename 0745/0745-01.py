Trie = lambda: defaultdict(Trie)
W = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for w, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[W] = w
                
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[W] = w

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            
            cur = cur[letter]
            
        return cur[W]
