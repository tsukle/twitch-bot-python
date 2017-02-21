import socket
import json
import database
from colorama import init, Fore, Back, Style
from time import sleep

init(autoreset=True)
s = socket.socket()
db = database

with open("settings_personal.json") as data:
    settings = json.load(data)

def setup():
    print(Fore.WHITE + """
                   Twitch Chat Bot                 
            By: Tsukle (http://tsukle.com)         
                    Version: 1.0
              (Don't resize the window.)""")                   
    print(Fore.WHITE + "____________________________________________________")

    print("")

#Connects to the twitch IRC and logs in also giving the channel name to join.
def createSocket():
    s.connect(("irc.twitch.tv", 6667))
    s.send(("PASS " + settings["authkey"] + "\r\n").encode())
    s.send(("NICK " + settings["username"] + "\r\n").encode())
    s.send(("CAP REQ :twitch.tv/membership\r\n").encode())
    s.send(("CAP REQ :twitch.tv/commands\r\n").encode())
    s.send(("CAP REQ :twitch.tv/tags\r\n").encode())
    s.send(("JOIN #" + settings["channel"] + "\r\n").encode())
    return s

#Bot sends a normal message to chat
def sendMessage(Message):
    Message = str(Message)
    msgConstruct = "PRIVMSG #" + settings["channel"] + " :" + Message
    s.send((msgConstruct + "\r\n").encode())
    print(Fore.BLACK + Back.YELLOW + " BOT " + Style.RESET_ALL + " > " + Message)
    sleep(1)

#Bot sends a special (coloured) message to chat
def sendSpecialMessage(Message):
    Message = str(Message)
    msgConstruct = "PRIVMSG #" + settings["channel"] + " :/me " + Message
    s.send((msgConstruct + "\r\n").encode())
    print(Fore.BLACK + Back.YELLOW + " BOT " + Style.RESET_ALL + " > " + Message)
    sleep(1)

#AFK response
def AFKCheck():
    msgConstruct = "PONG :tmi.twitch.tv"
    s.send((msgConstruct + "\r\n").encode())
    print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > AFK Check complete ")


def getInfo(line):
    

#Takes IRC line and splits it | returns name
def getUser(msg):
    return msg
    #spliced = msg.split(":", 2) #1: gets rid of the first colon it finds    2: gets rid of the first two it finds and splits it
    #user = spliced[1].split("!", 1)[0]
    #if("tmi.twitch.tv" in user):
        #user = "twitch"
       # return user
    #elif("tsuklebot" in user):
        #user = "bot"
       # return user
    #else:
        #return user


#Takes IRC line and splits it | returns message
def getMessage(msg):
    if("PING :tmi.twitch.tv" in msg):
        AFKCheck()

    else:
        message = msg
        #spliced = msg.split(":", 2) #1: gets rid of the first colon it finds    2: gets rid of the first two it finds and splits it
        #message = spliced[2]
        return str(message)

#Splices owner command and adds new command to database
def createCommand(msg):
    spliced = msg.split(" ", 2)
    command = spliced[1]
    response = spliced[2]
    if("!commands" in command or "!addcom" in command or "!delcom" in command):
        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Is a reserved command.")
    else:    
        dbResponse = db.addCommand(command, response)
        if (dbResponse != 0):
            print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Added to the database.")
        else:
            print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Error: " + str(dbResponse))

#Splices owner command and removes the command from the database
def deleteCommand(msg):
    spliced = msg.split(" ", 1)
    s2 = spliced[1]
    s3 = s2.split("\r", 2)
    command = s3[0]
    dbRes = db.removeCommand(command)
    if (dbRes == 1):
        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Removed from the database.")
    else:
        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Error: " + str(dbRes))

#Splices command and searches database for it
def execCommand(msg):
    spliced = msg.split("\r", 2)
    command = spliced[0]
    response = db.getCommand(command)
    if (response != 0):
        sendMessage(response)
    else:
        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Not found in the database.")