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
        if not p or not q:
            return False
        
        dp = deque([p])
        dq = deque([q])

        while dp and dq:
            if len(dp) != len(dq):
                return False

            for _ in range(len(dp)):
                node_p = dp.popleft()
                node_q = dq.popleft()
                
                if not node_p and not node_q:
                    continue
                if not node_p or not node_q or node_p.val != node_q.val:
                    return False
                
                dp.append(node_p.left)
                dq.append(node_q.left)
                dp.append(node_p.right)
                dq.append(node_q.right)
        return len(dp) == len(dq)