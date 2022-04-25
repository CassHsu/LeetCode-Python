class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.journey = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkin[id]
        self.journey[(start_station, stationName)][0] += (t - start_time)
        self.journey[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.journey[(startStation, endStation)]
        return total_time / total_trips
