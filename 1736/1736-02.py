class Solution:
    def maximumTime(self, time: str) -> str:
        res = [t for t in time]
        if res[0] == "?":
            res[0] = ("1" if res[1] != "?" and int(res[1]) > 3 else "2")
        if res[1] == "?":
            res[1] = ("3" if int(res[0]) > 1 else "9")
        if res[3] == "?":
            res[3] = "5"
        if res[4] == "?":
            res[4] = "9"
        return "".join(res)