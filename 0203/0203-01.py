class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
				dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = dummy.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
                
        return dummy.next
