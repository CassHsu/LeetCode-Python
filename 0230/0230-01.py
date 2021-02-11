class Solution:
    def kthSmallest(self, root, k):
        leftSize = self.getSize(root.left)
        if k <= leftSize:
            return self.kthSmallest(root.left, k)
        
        if k == leftSize + 1:
            return root.val
        
        return self.kthSmallest(root.right, k - (leftSize + 1))
        
    def getSize(self, root):
        if root == None:
            return 0
        return self.getSize(root.left) + 1 + self.getSize(root.right)