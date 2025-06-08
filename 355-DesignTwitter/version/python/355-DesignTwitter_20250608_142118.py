# Last updated: 08/06/2025, 14:21:18
from collections import defaultdict
import heapq
class Tweet:
    def __init__(self, tweet_id: int, timestamp: int):
        self.tweet_id = tweet_id
        self.timestamp = timestamp

class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.tweets = []           # List of Tweet objects (most recent first)
        self.followees = set()     # Set of user_ids this user follows

    def post_tweet(self, tweet):
        self.tweets.append(tweet)

    def follow(self, followee_id: int):
        self.followees.add(followee_id)

    def unfollow(self, followee_id: int):
        self.followees.discard(followee_id)

class Twitter:
    def __init__(self):
        self.users = {}        # user_id -> User object
        self.timestamp = 0 #gobalTimestamp

    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.users:
            self.users[userId] = User(userId)
        tweet = Tweet(tweetId, self.timestamp)
        self.users[userId].post_tweet(tweet)
        self.timestamp += 1

    def getNewsFeed(self, userId: int):
        if userId not in self.users:
            return []
        user = self.users[userId]
        tweets = []
        # Collect tweets from self and followees
        users_to_check = user.followees | {userId}
        for uid in users_to_check:
            if uid in self.users:
                tweets.extend(self.users[uid].tweets)
        # Sort and return up to 10 most recent
        tweets.sort(key=lambda t: t.timestamp, reverse=True)
        return [t.tweet_id for t in tweets[:10]]

    def follow(self, followerId: int, followeeId: int):
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)

    
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)