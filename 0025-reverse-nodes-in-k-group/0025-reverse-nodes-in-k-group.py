# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        group_prev=dummy

    # The get_kth_node helper finds the k-th node after group_prev (returns None if not enough nodes).
        def get_kth_node(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr
    # If kth exists, reverse the portion between group_prev.next and kth.
        while True:
            kth = get_kth_node(group_prev,k)
            if not kth:
                break
            group_next = kth.next

            #reverse group
            prev,curr=kth.next,group_prev.next
            while curr!=group_next:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            # After reversing, update pointers so the list remains correctly linked.
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp

        return dummy.next
        