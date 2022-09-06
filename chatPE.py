#Aurthor Marcus Palmer
#Date: 2022
#UWE Disertation

#applictaion import
from flask import Flask, render_template, request
import random
import csv
import os
from botConfig import myBotName, chatBG, botAvatar, useBlackboardSupport, confidenceLevel
from botRespondPE import getResponse

##Experimental Date Time
from dateTime import getTime, getDate

#Assign name to virtual assistant
chatbotName = myBotName

#Print evidence in CMD
print("Bot Name set to: " + chatbotName)
print("Confidence level set to " + str(confidenceLevel))


#Create Log file
botLog = os.path.abspath('uwevirtualassistant/BotLog.csv')
try:
    file = open(botLog, 'r')
except IOError:
    file = open(botLog, 'w')

app = Flask(__name__)

#If no virtual assistant 100% sure there is no answer then try this
def tryBlackboardSupport(myQuery):
	#print("<br>Try this from my friend Blackboard: <a target='_blank' href='" + j + "'>" + query + "</a>")
	return "<br>You can try this from Blackboard Support: <a target='_blank' href='https://info.uwe.ac.uk/online/blackboard/'>" + myQuery + "</a>"

# render these these variables in the template
@app.route("/")
def home():
    return render_template("index.html", botName = chatbotName, chatBG = chatBG, botAvatar = botAvatar)

#get theses responses and use the variable tryBlackboardSupport if there is no answer in dataset
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(getResponse(userText))
    if botReply is "IDKresponse":
        botReply = str(getResponse('IDKnull')) ##Send the i don't know code back to the DB
        if useBlackboardSupport == "yes":
            botReply = botReply + tryBlackboardSupport(userText)
            #Get time and date to print to log
    elif botReply == "getTIME":
        botReply = getTime()
        print(getTime())
    elif botReply == "getDATE":
        botReply = getDate()
        print(getDate())
    ##Log to CSV file
    print("Logging to CSV file now")
    with open('uwevirtualassistant/BotLog.csv', 'a', newline='') as logFile:
        newFileWriter = csv.writer(logFile)
        newFileWriter.writerow([userText, botReply])
        logFile.close()

        #return valid response
    return botReply
