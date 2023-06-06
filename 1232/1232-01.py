class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        
        dx = coordinates[1][0] - x0
        dy = coordinates[1][1] - y0
        
        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            
            if dy * (x - x0) != dx * (y - y0):
                return False
            
        return True
