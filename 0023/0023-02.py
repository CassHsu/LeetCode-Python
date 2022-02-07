class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for ll in lists:
            while ll:
                nodes.append(ll.val)
                ll = ll.next
                
        nodes.sort()
        head = ListNode()
        curr = head
        
        for n in nodes:
            curr.next = ListNode(n)
            curr = curr.next
        
        return head.next
