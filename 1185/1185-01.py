import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        w = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        d = datetime.date(day=day, month=month, year=year)
        return w[d.weekday()]
