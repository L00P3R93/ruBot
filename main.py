import tweepy
import os

auth = tweepy.OAuthHandler("2zrDuTOJvE6ylmKeJ8nbehGcf", "Npwt2nYLJ7RZRgASSlahZzWCiAkIhFSIbTiLr1LQ2A92nnXGaf")
auth.set_access_token("636861738-K1UELUqQoNMvD70tq6odZMSbWAyXvSahZi47Tsg8", "Myw4y9FDWxCZBxqsxRntuiFJHteF3l0LG8JwrC0G3KMeq")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Authentication OK')
except:
    print("Error during authentication")