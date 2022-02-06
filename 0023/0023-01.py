class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = curr = ListNode(0)
        
        for ll in lists:
            while ll:
                nodes.append(ll.val)
                ll = ll.next
                
        for n in sorted(nodes):
            curr.next = ListNode(n)
            curr = curr.next
            
        return head.next
