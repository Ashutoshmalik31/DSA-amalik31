class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = []
        pre = 1
        for num in range(len(nums)):
            pre = pre * nums[num]
            pre_prod.append(pre)
        
        post_prod = []
        post = 1
        for num in range(len(nums) - 1, -1, -1):
            post = post * nums[num]
            post_prod.append(post)
        post_prod = post_prod[::-1]

        final_result = []
        for i in range(len(nums)):
            if i-1 < 0:
                final_result.append(post_prod[i + 1])
            elif i + 1 == len(nums):
                 final_result.append(pre_prod[i - 1])
            else:
                final_result.append((pre_prod[i - 1]) * (post_prod[i + 1]))
        return final_result
        
        # pre_product = []
        # pre = 1
        # for num in range(len(nums)):
        #     pre = pre * nums[num]
        #     pre_product.append(pre)
        # print(pre_product)

        # post_product = []
        # post = 1
        # for num in range(len(nums) - 1, -1, -1):
        #     post = post * nums[num]
        #     post_product.append(post)
        # post_product = post_product[::-1]
        # print(post_product)

        # final_result = []
        # val = 1
        # for i in range(len(nums)):
        #     if i - 1 < 0:
        #         val = post_product[i + 1]
        #     elif i + 1 == len(nums):
        #         val = pre_product[i - 1]
        #     else:
        #         val = pre_product[i-1] * post_product[i+1]
        #     final_result.append(val)
        # return final_result