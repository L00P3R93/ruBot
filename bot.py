import tweepy,time, logging
from credentials import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweetlist = ['Test tweet one!', 'Test tweet two!', 'Test tweet three!']

for line in tweetlist:
    logger.info(f"Tweeting ... {line}")
    api.update_status(line)
    logger.info("Waiting ...")
    print(line)
    print('...')
    time.sleep(15)
logger.info("All Done!")