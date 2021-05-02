class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = (ord(coordinates[0]) - ord('a') + 1) % 2
        y = int(coordinates[1]) % 2
        
        return (x ^ y) == 1
