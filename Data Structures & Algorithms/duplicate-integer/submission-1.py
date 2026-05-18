class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        # seen = set()
        # if nums:
        #     for num in nums:
        #         if num in seen:
        #             return True
        #         else:
        #             seen.add(num)
        #     return False  
        # else:
        #     return False              