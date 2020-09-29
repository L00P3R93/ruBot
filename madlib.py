import json, io, tweepy, time, logging
from urllib.request import urlopen
from random import randint
from credentials import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

list1file = urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/mythology/greek_monsters.json')
list1read = list1file.read()

list2file = urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/menuItems.json')
list2read = list2file.read()

list3file = urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/humans/occupations.json')
list3read = list3file.read()

list1 = json.loads(list1read)['greek_monsters']
list2 = json.loads(list2read)['menuItems']
list3 = json.loads(list3read)['occupations']


poemlist = []
counter = 0

while counter < 5:
    list1num = randint(0, len(list1)-1)
    list2num = randint(0, len(list2)-1)
    list3num = randint(0, len(list3)-1)

    first = list1[list1num]
    second = list2[list2num].lower()
    third = list3[list3num].lower() + 's'

    poem = 'so much depends / upon / a %s / glazed with /%s /beside the / %s' % (first, second, third)

    #print(poem)
    poemlist.append(poem)
    counter = counter + 1

for line in poemlist:
    logger.info(f"Posting poem ... {line}")
    api.update_status(line)
    print(line)
    time.sleep(15)

logger.info("All Done!")