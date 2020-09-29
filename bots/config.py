import tweepy
import os
import logging

logger = logging.getLogger()


def create_api():
    consumer_key = "2zrDuTOJvE6ylmKeJ8nbehGcf"
    consumer_secret = "Npwt2nYLJ7RZRgASSlahZzWCiAkIhFSIbTiLr1LQ2A92nnXGaf"
    access_token = "636861738-K1UELUqQoNMvD70tq6odZMSbWAyXvSahZi47Tsg8"
    access_token_secret = "Myw4y9FDWxCZBxqsxRntuiFJHteF3l0LG8JwrC0G3KMeq"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
