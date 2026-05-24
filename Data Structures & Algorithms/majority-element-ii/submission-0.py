class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minimum_count = len(nums) // 3
        res = []
        for ele,freq in count.items():
            if freq > minimum_count:
                res.append(ele)
        return res
        