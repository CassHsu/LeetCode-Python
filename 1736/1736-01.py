class Solution:
    def maximumTime(self, time: str) -> str:
        res = ""
        m = { 0: "2",
              1: {"0": "9", "1": "9", "2": "3"},
              3: "5",
              4: "9"}
        res = ""
        for i, t in enumerate(time):
            if t == "?":
                if i == 0 and time[1] != "?" and int(time[1]) > 3:
                    res += "1"
                elif i == 1:
                    res += m[1][res[0]]
                else:
                    res += m[i]
            else:
                res += t
                
        return res