import tweepy, logging, time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

filename = open('quotes_1.txt','r', encoding='utf-8')
lines = filename.readlines()
filename.close()

logger.info("Initializing ...")
for line in lines[50:55]:
    logger.info(f"Posting ... {line}")
    api.update_status(line)
    print(line)
    time.sleep(30)

logger.info("All Done!")

