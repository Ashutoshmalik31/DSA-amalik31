# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False

        
        
        # dp = deque([p])
        # dq = deque([q])

        # while dp and dq:
        #     for _ in range(len(dp)):
        #         node_p = dp.popleft()
        #         node_q = dq.popleft()
        #         if node_p is None and node_q is None:
        #             continue
        #         if node_p is None or node_q is None or node_p.val != node_q.val:
        #             return False
        #         dp.append(node_p.left)
        #         dp.append(node_p.right)
        #         dq.append(node_q.left)
        #         dq.append(node_q.right) 
        # return True