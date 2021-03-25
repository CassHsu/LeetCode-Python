class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        m = {}
        m["type"] = 0
        m["color"] = 1
        m["name"] = 2
        
        count = 0
        for item in items:
            if item[m[ruleKey]] == ruleValue:
                count += 1
        
        return count
