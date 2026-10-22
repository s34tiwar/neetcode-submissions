from collections import defaultdict, deque
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        # in getnewsfeed we need to compare tweets from multiples users and return 10 most recent overal 
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        return 

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        # users own tweets 
        for tweet in self.tweets[userId]:
            all_tweets.append(tweet)
        # tweets from people they follow 
        for followId in self.following[userId]:
            for tweet in self.tweets[followId]:
                all_tweets.append(tweet)
        # newest firs by time one tweet = []
        all_tweets.sort(reverse=True)
        res = []
        for time, tweetId in all_tweets[:10]:
            res.append(tweetId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
