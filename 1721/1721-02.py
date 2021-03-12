class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1 = None
        n2 = None
        curr = head
        
        while curr:
            k -= 1
            if n2 != None:
                n2 = n2.next
            
            if k == 0:
                n1 = curr
                n2 = head
            curr = curr.next
            
        n1.val, n2.val = n2.val, n1.val
        return head
