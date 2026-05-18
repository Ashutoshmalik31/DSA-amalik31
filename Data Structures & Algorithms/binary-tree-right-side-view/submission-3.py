# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        res = []
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            if level:
                res.append(level[-1])
        return res
                 
       
       
       
       
       
       
        # res = []

        # if not root:
        #     return []
        
        # dq = deque()
        # dq.append(root)
        # while dq:
        #     level = []
        #     for _ in range(len(dq)):
        #         node = dq.popleft()
        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)
        #         level.append(node.val)
        #     if level:
        #         res.append(level[-1])
                
        # return res