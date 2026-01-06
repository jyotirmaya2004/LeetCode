# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        level = 0
        q.append(root)
        max_sum = float("-inf")
        res = float("infinity")

        while q :
            qlen = len(q)
            level_sum =0
            while qlen>0:
                cur = q.popleft()
                level_sum+=cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

                
                qlen-=1
            level+=1
            if level_sum >max_sum:
                max_sum = level_sum
                res = level
        return res

    
        