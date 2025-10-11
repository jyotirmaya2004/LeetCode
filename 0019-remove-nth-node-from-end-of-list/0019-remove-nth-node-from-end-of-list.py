# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Count total nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        # Step 2: Find position from start (1-indexed)
        pos = count - n
        
        # Step 3: If we need to remove the head node
        if pos == 0:
            return head.next
        
        # Step 4: Traverse again to (pos - 1)-th node
        temp = head
        for _ in range(pos - 1):
            temp = temp.next
        
        # Step 5: Remove the nth node from end
        if temp.next:
            temp.next = temp.next.next
        
        return head
