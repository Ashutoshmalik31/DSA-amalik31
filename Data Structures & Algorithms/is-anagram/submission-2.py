class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = self.char_counter(s)
        t1 = self.char_counter(t)
        if s1 == t1:
            return True
        return False

    def char_counter(self, test):
        count = {}
        for i in test:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1  
        return count              