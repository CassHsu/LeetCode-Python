class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        stack = []
        
        while fast and fast.next:
            
            stack.append(slow.val)
            
            slow = slow.next
            fast = fast.next.next
        
        # len is even
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val != stack.pop():
                return False
            
            slow = slow.next
            
        return True
