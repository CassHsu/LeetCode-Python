class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1, a2 = [], []
        while l1:
            a1.append(l1.val)
            l1 = l1.next
            
        while l2:
            a2.append(l2.val)
            l2 = l2.next
        
        m = 1
        n1 = 0
        for n in a1:
            n1 += (n * m)
            m *= 10
            
        m = 1
        n2 = 0
        for n in a2:
            n2 += (n * m)
            m *= 10
        
        node = ListNode()
        head = node
        
        rs = str(n1 + n2)[::-1]
        for s in rs:
            node.next = ListNode(s)
            node = node.next
            
        return head.next
