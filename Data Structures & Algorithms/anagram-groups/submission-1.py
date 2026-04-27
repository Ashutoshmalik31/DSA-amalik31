class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for chr in str:
                count[ord(chr) - ord("a")] += 1
            seen[tuple(count)].append(str)
        return list(seen.values())
        
        
        





















        
        
        
        
        
        
        
        # seen = defaultdict(list)
        # for str in strs:
        #     count = [0] * 26
        #     for c in str:
        #         count[ord(c) - ord("a")] += 1
        #     seen[tuple(count)].append(str)
        # return list(seen.values())

# NOTE: My solution did not work because the key of dictionary cannot be 
# immutable and the dictionary that I get from char_counter function was
# returning a dict. which i was planning to use for grouping anagrams. 
    #     seen = set()
    #     i = 0
    #     j = 1
    #     result = []
    #     for i in range(len(nums) - 2):
    #         for j in range(len(nums) - 1):
    #             s1 = self.char_counter(nums[i])
    #             if self.char_counter(nums[j]) == s1:
    #                 result.append(s1)
    #     return result

    # def char_counter(self, test):
    #     count = {}
    #     for i in test:
    #         if i in count:
    #             count[i] += 1
    #         else:
    #             count[i] = 1  
    #     return count    
