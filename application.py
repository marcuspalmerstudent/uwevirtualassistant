#Aurther Marcus Palmer
# Date: 2022
# UWE Disertation
-->
#! /usr/bin/python3

#Use Flask
from flask import Flask, render_template, request

# Import these modules
import random
import csv
import os

#Access these files
from botConfig import myBotName, chatBG, botAvatar, useBlackboardSupport, confidenceLevel
from botRespond import getResponse

##Experimental Date Time
from dateTime import getTime, getDate

# Application name
application = Flask(__name__)

# Virtal assistant name
chatbotName = myBotName

# Output
print("Bot Name set to: " + chatbotName)
print("Background is " + chatBG)
print("Avatar is " + botAvatar)
print("Confidence level set to " + str(confidenceLevel))

#Create Log file
try:
    file = open('BotLog.csv', 'r')
except IOError:
    file = open('BotLog.csv', 'w')

#If no answer found try this
def tryBlackboardSupport(myQuery):
	#print("<br>Try this from Blackboard: <a target='_blank' href='" + j + "'>" + query + "</a>")
	return "<br><br>You can try this from Blackboard Support: <a target='_blank' href='https://info.uwe.ac.uk/online/blackboard/'>" + myQuery + "</a>"

#Render template
@application.route("/")
def home():
    return render_template("index.html", botName = chatbotName, chatBG = chatBG, botAvatar = botAvatar)

#Get responses
@application.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(getResponse(userText))
    if botReply is "IDKresponse":
        botReply = str(getResponse('IDKnull')) ##Send the i don't know code back to the DB
        if useBlackboardSupport == "yes":
            botReply = botReply + tryBlackboardSupport(userText)
    elif botReply == "getTIME":
        botReply = getTime()
        print(getTime())
    elif botReply == "getDATE":
        botReply = getDate()
        print(getDate())
    ##Log to CSV file
    print("Logging to CSV file now") #Print in CMD
    with open('BotLog.csv', 'a', newline='') as logFile: #Print in log file
        newFileWriter = csv.writer(logFile)
        newFileWriter.writerow([userText, botReply])
        logFile.close()
    return botReply

#Run application
if __name__ == "__main__":
    application.run()
