import tweepy, time, logging
from credentials import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

filename = open('quotes_1.txt', 'r',encoding='utf-8')
tweettext = filename.readlines()
filename.close()

logger.info("Initiating ...")
for line in tweettext[10:15]:
    logger.info(f"Posting tweet ...{line}")
    api.update_status(line)
    print(line)
    time.sleep(15)

logger.info("All Done!")

