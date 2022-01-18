class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for w in title.split(" "):
            if len(w) < 3:
                ans.append(w.lower())
            else:
                ans.append(w.capitalize())
                
        return " ".join(ans)
