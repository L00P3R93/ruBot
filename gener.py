import tweepy, logging, time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler("2zrDuTOJvE6ylmKeJ8nbehGcf", "Npwt2nYLJ7RZRgASSlahZzWCiAkIhFSIbTiLr1LQ2A92nnXGaf")
auth.set_access_token("636861738-K1UELUqQoNMvD70tq6odZMSbWAyXvSahZi47Tsg8", "Myw4y9FDWxCZBxqsxRntuiFJHteF3l0LG8JwrC0G3KMeq")
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

