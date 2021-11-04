class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        curr = head
        for i in range(k - 1, len(arr), k):
            for j in range(i, i - k, -1):
                curr.val = arr[j]
                curr = curr.next
                
        return head
