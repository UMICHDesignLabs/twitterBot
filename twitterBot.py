import re, random, tweepy
import inflect
from PIL import Image
import urllib
p = inflect.engine()

views = []

def smart_truncate(content, length=80, suffix=u'\u2026'.encode('utf-8')):
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0]+suffix

class Item:
    def __init__(self, cIn, collectionIn, itemIDIn, imageIDIn, nameIn, dateIn):
        self.c = cIn
        self.collection = collectionIn
        self.imageID = imageIDIn
        self.itemID = itemIDIn
        self.name = nameIn
        self.date = dateIn

############## get into Twitter ###############

auth = tweepy.OAuthHandler("WMNAYBraGHz1a56HGHzJIUYOC", "ci5TW0jg0w3nAuMZF8DqoYFb7ovKPUNrTTQ0em3e6B7Nuz2TFx")
auth.set_access_token('4355370562-ZrSnI2pB7XNVglUeBCZNkUrKpgjxDkMyuUpnTzT', 'ck7x1L71hBJfTMNuun7VeQDwGIcZwBBwbMH3oGytGxuzD')

api = tweepy.API(auth)

################## Input ######################

allItems = []

import csv
f = open('metadata1.csv')
csv_f = csv.reader(f)

for row in csv_f:
    #each row in csv is formatted as: [collection, itemID, imageID, name, date]
    itexX = Item(row[0], row[1], row[2], row[3], row[4], row[5])
    allItems.append(itemX)

ifile.close()

################## Write Tweet ######################

randomNumber = random.randrange(0, len(allItems) - 1)
randomImage = allItems[randomNumber]
c = randomImage[0]
collection = randomImage[1]
itemID = randomImage[2]
imageID = randomImage[3]
name = randomImage[4]
date = randomImage[5]

# Format of UM Library Image URL
# EX: http://quod.lib.umich.edu/cgi/i/image/api/image/sclaudubon/B6719889/29377_0001/full/!530,530
imageurl = "http://quod.lib.umich.edu/cgi/i/image/api/image/" + collection + "/" + imageID + "/" + itemID +"/full/!530,530"

# Format of URL
# EX: http://quod.lib.umich.edu/  s/sclaudubon/   x-  B6719889    /   29377_0001
url = "http://quod.lib.umich.edu/" + c + "/" + collection + "/x-" + imageID + "/" + imageID + "/" + itemID

# check to make sure date isn't empty
if not date:
    date = "Date Unknown"

status = name + "(" + date + ")" + url

################## Access Image ####################

# save image as JPG and covert to GIF (for some reason Twitter didn't like jpegs)
print imageurl
urllib.urlretrieve(imageurl, "image.jpg")
im = Image.open('image.jpg')
im.save('image.gif','GIF')

#if status with name is too long, truncate name, try again
if (len(status) > 120):
    status = smart_truncate(name) + " (" + str(date) + ") " + location
print status

##################### Output ######################

#Upload the image to Twitter along with the metadata
api.update_with_media('image.gif',status=status)














