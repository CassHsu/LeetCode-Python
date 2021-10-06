class Solution:
    img = []
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.img = image
        self.findTarget(len(image), len(image[0]), sr, sc, image[sr][sc])
        self.fillNew(newColor)
        return self.img
    
    # fill -1
    def findTarget(self, rSize, cSize, sr, sc, target):
        if sr < 0 or sr >= rSize or sc < 0 or sc >= cSize:
            return
        
        if self.img[sr][sc] != target:
            return
        
        self.img[sr][sc] = -1
        
        self.findTarget(rSize, cSize, sr - 1, sc, target)
        self.findTarget(rSize, cSize, sr + 1, sc, target)
        self.findTarget(rSize, cSize, sr, sc - 1, target)
        self.findTarget(rSize, cSize, sr, sc + 1, target)
    
    def fillNew(self, newColor):
        for i, row in enumerate(self.img):
            for j, c in enumerate(row):
                if c == -1:
                    self.img[i][j] = newColor
