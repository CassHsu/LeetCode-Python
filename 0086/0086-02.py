class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lt, rt = left, right
        
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                rt.next = head
                rt = rt.next
                
            head = head.next
            
        lt.next = right.next
        rt.next = None
        
        return left.next
