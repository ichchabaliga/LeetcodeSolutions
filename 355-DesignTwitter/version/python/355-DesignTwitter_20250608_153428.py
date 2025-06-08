# Last updated: 08/06/2025, 15:34:28
# 10 tweets
# user cant follow self 

# Requirements: 
# follow/unfollow
# post a tweet 
# userFeed

# tweet
# user
# twitter


class Tweet:
    def __init__(self,tweet_id,timestamp,content):
        self.tweet_id=tweet_id
        self.timestamp=timestamp
        self.content=content
class User:
    def __init__(self,userId):
        self.userId = userId
        self.tweets = []
        self.followees = set()
    def post_tweet(self,tweet:Tweet):
        self.tweets.append(tweet)



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
    
    def follow(self,followeeID):
        self.followees.add(followeeID)
    
    def unfollow(self,followeeID):
        self.followees.remove(followeeID)
 

class Twitter:
    def __init__(self):
        self.users ={ } # user_id -> User
        self.timestamp = 0
    
    def addUser(self,userId):
        self.users[userId]=User(userId)
    
    def delUser(self,userId):
        del self.users[userId]


    def postTweet(self, userId, tweetId, tweetContent=''):
        if not userId in self.users:
            self.addUser(userId)
        newTweet=Tweet(tweetId,self.timestamp, tweetContent)
        self.users[userId].post_tweet(newTweet)
        self.timestamp+=1
    
    def getNewsFeed(self,userId):
        if userId not in self.users:
            return []
        heap=[]
        relevant_users={userId} | self.users[userId].followees
        print(relevant_users)
        print()
        for user in relevant_users:
            userObj=self.users[user]
            if not userObj:
                continue
            for tweet in reversed(userObj.tweets):
                if len(heap)<10:
                    heapq.heappush(heap,(tweet.timestamp,tweet.tweet_id))
                else:
                    if tweet.timestamp > heap[0][0]:
                        heapq.heappushpop(heap,(tweet.timestamp,tweet.tweet_id))
                    else:
                        break

        return [tweet_Id for _,tweet_Id in sorted(heap,reverse=True, key=lambda x:x[0])][:10]

        
    
    
    
    
    def follow(self,followerID,followeeID):
        if followerID==followeeID:
            return
        if  not followerID in self.users:
            self.addUser(followerID)
        if not followeeID in self.users:
            self.addUser(followeeID)


        self.users[followerID].followees.add(followeeID)


    def unfollow(self,followerId,followeeId):
        if self.users[followerId] and followeeId in self.users[followerId].followees:
            self.users[followerId].followees.remove(followeeId)
    
