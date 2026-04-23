class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            prefix.append(prod)
        prod = 1
        for j in range(len(nums)-1, -1 ,-1):
            prod = prod * nums[j]
            postfix.append(prod)
        postfix = postfix[::-1]
        solution = []
        for i in range(len(nums)):
            product = 1
            if i-1 < 0:
                product = postfix [i+1]
            elif i+1 == len(nums):
                product = prefix[i - 1]
            else:
                product = prefix[i-1] * postfix [i+1]
            solution.append(product)
        return solution