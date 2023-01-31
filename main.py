import tweepy
consumer_key= 'Nsmi67mm5dl7ssD1S4Ko3v8nz'
consumer_secret= 'dbH90iinf7GjO1QXuDO03VzMCqvi1x33HtsjheAs3269qxzBSd'
access_token= '1618423209493434369-pPvP6sXAyGwOU8ptlj7Kyeiy1qFjfM'
access_token_secret= 'RbN7rKZRhYbEGHgfUWi9pvEvaoJ70JbYVqEimvDFulOXY'

bearer_token= 'AAAAAAAAAAAAAAAAAAAAABTNlQEAAAAAu3ns4qekfXQEN1OFO1l%2FBe8eALw%3DwEJzomnagfqdB0cPmClq0Gh43lT9LdK3S9FXaPGEwPR5JxmEe9'
client = tweepy.Client(bearer_token=bearer_token)
#client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)
query = '#Software Engineer'
tweets = client.search_recent_tweets(query=query, max_results=10)
num = 0
with open("output.txt", "w") as f:
    for tweet in tweets.data:
        num += 1
        f.write(str(num) + ": " + tweet.text + '\n')