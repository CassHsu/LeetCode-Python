class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        il = k-1
        ir = len(values) - k
        
        curr = head
        i = 0
        while curr:
            if i == il:
                curr.val = values[ir]
            if i == ir:
                curr.val = values[il]
                
            curr = curr.next
            i += 1
        
        return head
