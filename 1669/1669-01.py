class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        for _ in range(a-1):
            start = start.next
        
        end = start.next
        for _ in range(a, b):
            end = end.next
        
        start.next = list2
        while list2.next:
            list2 = list2.next
        
        list2.next = end.next
        return list1
