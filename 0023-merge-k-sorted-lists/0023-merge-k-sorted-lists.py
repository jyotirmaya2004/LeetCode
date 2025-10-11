# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = defaultdict(list)
        for linked_list in lists:
            head = linked_list
            while head:
                nodes[head.val].append(head)
                temp = head
                head = temp.next
                temp.next = None
        next_node = None
        first_node = None
        for key in sorted(nodes.keys()):
            node_list = nodes[key]
            for node in node_list:
                if not next_node:
                    first_node = node
                    next_node = node
                    continue
                next_node.next = node
                next_node = node
        return first_node
