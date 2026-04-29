class Twitter:
    def __init__(self):
        self.followerMap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followerMap[userId].add(userId)
        for followeeID in self.followerMap[userId]:
            if followeeID in self.tweetmap:
                index = len(self.tweetmap[followeeID]) - 1
                count, tweetID = self.tweetmap[followeeID][index]
                minheap.append([count, tweetID, followeeID, index - 1])
        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count, tweetID, followeeID, index = heapq.heappop(minheap)
            res.append(tweetID)
            if index >= 0:
                count, tweetID = self.tweetmap[followeeID][index]
                heapq.heappush(minheap, [count, tweetID, followeeID, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)

    
    # def __init__(self):
    #     self.count = 0
    #     self.tweetmap = defaultdict(list)
    #     self.followmap = defaultdict(set)

    # def postTweet(self, userId: int, tweetId: int) -> None:
    #     self.tweetmap[userId].append([self.count, tweetId])
    #     self.count -= 1

    # def getNewsFeed(self, userId: int) -> List[int]:
    #     res = []
    #     minheap = []
    #     self.followmap[userId].add(userId)
    #     for followeeId in self.followmap[userId]:
    #         if followeeId in self.tweetmap:    
    #             index = len(self.tweetmap[followeeId]) - 1
    #             count, tweetId = self.tweetmap[followeeId][index]
    #             minheap.append([count, tweetId, followeeId, index-1])
    #     heapq.heapify(minheap)
    #     while minheap and len(res) < 10:
    #         count, tweetID, followeeId, index = heapq.heappop(minheap)
    #         res.append(tweetID)
    #         if index >= 0:
    #             count, tweetId = self.tweetmap[followeeId][index]
    #             heapq.heappush(minheap,[count, tweetId, followeeId, index-1])
    #     return res

    # def follow(self, followerId: int, followeeId: int) -> None:
    #     self.followmap[followerId].add(followeeId)

    # def unfollow(self, followerId: int, followeeId: int) -> None:
    #     if followeeId in self.followmap[followerId]:
    #         self.followmap[followerId].remove(followeeId)
        
