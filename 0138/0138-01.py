class Solution:
    visitedHash = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        n = Node(head.val, None, None)
        self.visitedHash[head] = n
        
        n.next = self.copyRandomList(head.next)
        n.random = self.copyRandomList(head.random)
        
        return n
