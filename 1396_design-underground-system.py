class UndergroundSystem:

    def __init__(self):
        self.checkin_pending={}
        self.station_average={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_pending[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        source,starttime=self.checkin_pending[id]
        key=(source,stationName)
        if key not in self.station_average:
            self.station_average[key]=[0,0]
        self.station_average[key][0]+=t-starttime
        self.station_average[key][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key=(startStation,endStation)
        return self.station_average[key][0]/self.station_average[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)