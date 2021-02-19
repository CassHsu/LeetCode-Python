class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        odd = head
        even = odd.next
        evenHead = even
        
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = evenHead
        return head
