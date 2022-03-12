class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        count = 1
        ite = head
        while ite.next:
            count += 1
            ite = ite.next
            
        k %= count
        if k == 0:
            return head
        
        p1, p2 = head, head
        for _ in range(k):
            p2 = p2.next
            
        while p2 and p2.next:
            p2 = p2.next
            p1 = p1.next
            
        res = p1.next
        p1.next = None
        p2.next = head
        
        return res
