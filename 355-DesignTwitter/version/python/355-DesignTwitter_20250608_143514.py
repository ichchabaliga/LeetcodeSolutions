# Last updated: 08/06/2025, 14:35:14
from collections import defaultdict
import heapq

class Tweet:
    def __init__(self, tweet_id: int, timestamp: int):
        self.tweet_id = tweet_id
        self.timestamp = timestamp

class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.tweets = []  # Stores up to 10 most recent tweets (oldest first)
        self.followees = set()

    def post_tweet(self, tweet: Tweet):
        """Add tweet and maintain only last 10 tweets"""
        self.tweets.append(tweet)
        if len(self.tweets) > 10:
            self.tweets.pop(0)  # Remove oldest tweet

class Twitter:
    def __init__(self):
        self.users = defaultdict(lambda: None)  # user_id -> User
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.users[userId]:
            self.users[userId] = User(userId)
        new_tweet = Tweet(tweetId, self.timestamp)
        self.users[userId].post_tweet(new_tweet)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        if not self.users[userId]:
            return []
        
        heap = []
        relevant_users = {userId} | self.users[userId].followees
        
        for uid in relevant_users:
            user = self.users[uid]
            if not user:
                continue
            
            # Process tweets in reverse chronological order (newest first)
            for tweet in reversed(user.tweets):
                if len(heap) < 10:
                    heapq.heappush(heap, (tweet.timestamp, tweet.tweet_id))
                else:
                    if tweet.timestamp > heap[0][0]:
                        heapq.heappushpop(heap, (tweet.timestamp, tweet.tweet_id))
                    else:
                        break  # Older tweets can't make it into the feed
        
        # Return tweets sorted newest first
        return [tweet_id for _, tweet_id in sorted(heap, reverse=True, key=lambda x: x[0])][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if not self.users[followerId]:
            self.users[followerId] = User(followerId)
        self.users[followerId].followees.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.users[followerId] and followeeId in self.users[followerId].followees:
            self.users[followerId].followees.remove(followeeId)
