class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = []
        right = []
        
        while head:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
                
            head = head.next
        
        total = left + right
        if len(total) <= 0:
            return None
        
        h = ListNode(total[0])
        curr = h
        
        
        for v in total[1:]:
            curr.next = ListNode(v)
            curr = curr.next
            
        return h
