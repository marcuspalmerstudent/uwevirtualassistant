#Aurthor Marcus Palmer
#Date: 2022
#UWE Disertation

#Import these files libraries and modules
from botConfig import confidenceLevel
from difflib import SequenceMatcher
import csv
import random
import os

#Use SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getResponse(sendMsg):
    #return "You said: " + sendMsg
    #Loop through CSV knowledge file.  If a question is equal to or greater than the confidence level, add it to a list of possible responses. Then return a random responses
    lineCount = 0
    successCount = 0
    exactCount = 0
    comeBacks = []
    exactReply = []
    exactMatch = .9

    botBrain = os.path.abspath('uwevirtualassistant/data/chatbot.csv')

    #use variable g as virtual assistant
    with open(botBrain) as g:

        #use csv reader
        lines = csv.reader(g)

        #easch line is class as virtual assistant and student
        for line in lines:

            #there are only two lines user as line 0 and virtual assistant line 1
            lineCount += 1

            #If there is no input empty count
            if not line[0] or not line[1]:
                emptyCount += 1

                #print warning in cmd
                print("WARNING: I had to skip row #" + str(lineCount) + " due to missing data.")

                #if there is a matc h to the query issue reply
            if lineCount > 1 and line[0] and line[1]:
                userText = line[0]
                botReply = line[1]
                checkMatch = similar(sendMsg, userText)
                if checkMatch >= exactMatch:
                    exactCount += 1
                    exactReply.append(botReply)

                    #print the followingin cmd
                    print("Likely match: " + userText)
                    print("Match is: " + str(checkMatch))

                    #if match is to confidece level then submit answer
                elif checkMatch >= confidenceLevel:
                    successCount += 1
                    comeBacks.append(botReply)
                    print("Possible match: " + userText)
                    print("Match is: " + str(checkMatch))
    if exactCount >= 1:
        botResponsePick = random.choice(exactReply)
    elif successCount >= 1:
        botResponsePick = random.choice(comeBacks)

        #if virtual assistant is 100% sure there is no match issue i dont know text
    else:
        botResponsePick = "IDKresponse"
    return botResponsePick
