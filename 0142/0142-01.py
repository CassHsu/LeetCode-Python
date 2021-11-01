class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            
            if slow == fast:
                break
                
        if not slow or not fast or slow != fast:
            return None
            
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
