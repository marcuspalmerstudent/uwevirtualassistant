#Aurthor Marcus Palmer
#Date: 2022
#UWE Disertation
#
#! /usr/bin/python3

#For getting the spreadsheet data from csv
import os
import csv
import sys

#For logging the queries and responses
import logging
logging.basicConfig(level=logging.INFO)

#Print in CMD
print('Do you want train your bot using recent conversation logs?')
userConfirm = input('Press y or n: ')

#Question in CMD whilst training
if(userConfirm != "y" and userConfirm != "Y"):
    print('Now exiting log training mode...')
    sys.exit()

#Add open this log for training previous queries better
with open('BotLog.csv') as g:
    lines = csv.reader(g)
    for line in lines:
        userText = line[0]
        botReply = line[1]
        print('##################################################')
        print('User said: ' + userText)
        print('Bot replied: ' + botReply)
        print('##################################################')
        print('To add/ retrain, type the new response, then press Enter.')
        print('To keep/ignore this response, press enter')
        print('##################################################')
        updateResponse = input('Update Response: ')
        if(updateResponse != ""):
            with open('data/chatbot.csv', 'a', newline='') as logFile:
                newFileWriter = csv.writer(logFile)
                newFileWriter.writerow([userText, updateResponse])
                #logFile.close()

print('##################################################')
print("I am all trained up and ready to chat!")
print("If on PythonAnywhere, you may need to restart the application.")
print('##################################################')

print('Shall I delete the recent conversation logs?')
userConfirm = input('Press y or n: ')

if(userConfirm != "y" and userConfirm != "Y"):
    print('Now exiting log training mode...')
    sys.exit()
else:
    #Remove log data
    if os.path.exists("BotLog.csv"):
        os.remove("BotLog.csv")
        print("I removed the recent chat logs.")