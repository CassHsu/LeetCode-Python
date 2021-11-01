class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
                
            if l2:
                carry += l2.val
                l2 = l2.next
            
            curr.next = ListNode(carry % 10)
            
            carry = 1 if carry >= 10 else 0 
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(carry)
            
        return dummy.next
