class Twitter:

    def __init__(self):
        self.tweets_map = defaultdict(deque)
        self.followers_map = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_map[userId].append((self.time, userId, tweetId))
        self.time += 1
        while len(self.tweets_map[userId]) > 10:
            self.tweets_map[userId].popleft()


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        temp_heap = []
        rel_users = {userId}
        for i in self.followers_map.get(userId, set()):
            rel_users.add(i)
        for u in rel_users:
            for t in self.tweets_map[u]:
                heapq.heappush(temp_heap,t)
                if len(temp_heap) > 10:
                    heapq.heappop(temp_heap)
        while temp_heap:
            res.append(heapq.heappop(temp_heap)[2])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers_map:
            self.followers_map[followerId].add(followeeId)
        else:
            self.followers_map[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_map[followerId]:
            self.followers_map[followerId].discard(followeeId)
