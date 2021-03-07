class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ite = head
        while ite:
            tmp = ite.next
            while tmp and tmp.val == ite.val:
                tmp = tmp.next
                
            ite.next = tmp
            ite = ite.next
        return head
