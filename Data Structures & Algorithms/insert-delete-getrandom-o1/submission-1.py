class RandomizedSet:

    def __init__(self):
        self.newmap = {}
        self.newlist = []

    def insert(self, val: int) -> bool:
        res = val not in self.newmap
        if res:
            self.newmap[val] = len(self.newlist) 
            self.newlist.append(val)
        return True

    def remove(self, val: int) -> bool:
        res = val in self.newmap
        if res:
            idx = self.newmap[val]
            lastval = self.newlist[-1]
            self.newlist[idx] = lastval
            self.newlist.pop()
            self.newmap[lastval] = idx
            del self.newmap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.newlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()