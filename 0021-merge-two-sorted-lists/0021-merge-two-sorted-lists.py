# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        curr1 = list1
        curr2 = list2
        prev = None
        head = None

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                newnode = curr1     
                curr1 = curr1.next
            else:
                newnode = curr2    
                curr2 = curr2.next

            if prev:
                prev.next = newnode
            else:
                head = newnode
            prev = newnode

        # Attach remaining nodes
        if curr1:
            prev.next = curr1
        else:
            prev.next = curr2

        return head
