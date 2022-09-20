#Aurthor Marcus Palmer
#Date: 2022
#UWE Disertation

#! /usr/bin/python3
#Import these libraries and modules
import urllib.request
from urllib.parse import urlparse
from os.path import splitext, basename
import os
from PIL import Image

#URL for avatar image
imageURL = input("Please paste the url of this image: ")

#Parse url
parsed = urlparse(imageURL)
root, ext = splitext(parsed.path)
imageExt = ext[1:]

#In cmd print the following
print("This is a " + imageExt + "file.")

urllib.request.urlretrieve(imageURL, "avatar." + imageExt)

#Does the file exist yet?
exists = os.path.isfile('static/bot.png')

#Convert to png
if imageExt == 'png':
    ##Move to replace the avatar file
    if exists:
        os.remove('static/bot.png')
    os.rename('avatar.png','static/bot.png')
    print('Success! Your ChatBot avatar has been updated.')
elif imageExt == 'jpg':
    #Convert to png
    if exists:
        os.remove('static/bot.png')
    image = Image.open('avatar.jpg')
    image.save('static/bot.png')
    os.remove('avatar.jpg')
    print('Success! Your ChatBot avatar has been updated.')
elif imageExt == 'gif':
    #convert to png
    if exists:
        os.remove('static/bot.png')
    image = Image.open('avatar.gif')
    image.save('static/bot.png')
    os.remove('avatar.gif')
    print('Success! Your ChatBot avatar has been updated.')
else:


    #Remove avatar
    os.remove("avatar." + imageExt)
    print("I couldn't do anything with that file.")