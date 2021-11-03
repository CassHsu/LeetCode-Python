class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            newPair = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = newPair
            prev.next = second
            
            prev = curr
            curr = newPair
            
        return dummy.next
