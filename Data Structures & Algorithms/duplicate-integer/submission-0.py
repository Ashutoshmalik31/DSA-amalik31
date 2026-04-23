class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        if nums:
            for num in nums:
                if num in seen:
                    return True
                else:
                    seen.add(num)
            return False  
        else:
            return False              