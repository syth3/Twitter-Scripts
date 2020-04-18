import os
import twitter

consumer_key = os.environ.get('CONSUMER_KEY')
print(consumer_key)

# consumer_secret = os.environ["CONSUMER_SECRET"]
# access_token = os.environ["ACCESS_TOKEN"]
# access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
#
#
# api = twitter.Api(consumer_key=[consumer_key],
#                   consumer_secret=[consumer_secret],
#                   access_token_key=[access_token],
#                   access_token_secret=[access_token_secret])