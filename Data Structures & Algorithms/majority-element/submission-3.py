class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res = defaultdict(int)
        # for num in nums:
        #     if num in res:
        #         res[num] += 1
        #     else:
        #         res[num] = 1
        # print(res)
        #
        # for key, value in res.items():
        #     if value >= (len(nums) / 2):
        #         return key

        ## Boyer - Moore Algorithm
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
                count = 1
            elif num == res:
                count += 1
            elif num != res:
                count -= 1
        return res