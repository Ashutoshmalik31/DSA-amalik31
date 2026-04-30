class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0,[],0)
        return res

        
        # res = []

        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return
        #     if i >= len(nums) or total > target:
        #         return

        #     cur.append(nums[i]) 
        #     dfs(i, cur, total + nums[i])
        #     cur.pop()
        #     dfs(i+1, cur, total)

        # dfs(0, [], 0)
        # return res