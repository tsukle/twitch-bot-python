import socket
import json
import database
from colorama import init, Fore, Back, Style
from time import sleep

#------------------------------------------------------------------------------------------------
# Initial Settings
init(autoreset=True)

#------------------------------------------------------------------------------------------------
# Variables & extra inits
s = socket.socket()
db = database
db.createTable()

#------------------------------------------------------------------------------------------------
# Open JSON settings file
with open("settings_personal.json") as data:
    opt = json.load(data)


#------------------------------------------------------------------------------------------------
# Create an IRC connection and view Chat
def connect():
    s.connect(("irc.twitch.tv", 6667))
    s.send(("CAP REQ :twitch.tv/membership\r\n").encode())
    s.send(("CAP REQ :twitch.tv/commands\r\n").encode())
    s.send(("CAP REQ :twitch.tv/tags\r\n").encode())
    s.send(("PASS " + opt["authkey"] + "\r\n").encode())
    s.send(("NICK " + opt["username"] + "\r\n").encode())
    s.send(("JOIN #" + opt["channel"] + "\r\n").encode())
    return s

def chat():
    display = "".encode()
    con = connect()
    while True:
        display = con.recv(1024)
        display = display.decode()
        message = display.split("\n")
        display = display.encode()
        display = message.pop()

        for line in message:
            response = info(line)
            if(response["display-name"] == "twitch" or response["display-name"].lower() == opt["username"]):
                a = 1
            else:
                print(Back.WHITE + Fore.BLACK + " " + response["display-name"] + " " + Style.RESET_ALL + " > " + response["message"])
                yield response

#------------------------------------------------------------------------------------------------
# Bot events
def send(message, sp = None): # Send a chat message (if s is true, the message with append /me)
    if(sp is None):
        construct = "PRIVMSG #" + opt["channel"] + " :" + message + "\r\n"
        s.send((construct).encode())
        print("Sent > " + message)
        sleep(1.5)
    else:
        construct = "PRIVMSG #" + opt["channel"] + " :/me " + message + "\r\n"
        s.send((construct).encode())
        print("Sent > " + message)
        sleep(1.5)

def afk(): # This responds to Twitch's afk PING requests.
    construct = "PONG :tmi.twitch.tv\r\n"
    s.send((construct).encode())


#------------------------------------------------------------------------------------------------
# Message information
def info(uin):
    if(uin.startswith("@badges")):
        info = {} #This will be returned eventually.

        inputSplit = uin.split(":") # Any input from the user will always give 5 objects, the rest are from twitch.

        # Gets the message sent and the channel it was sent from.
        if(":jtv MODE" in uin or "GLOBALUSERSTATE" in uin or "USERSTATE" in uin or "ROOMSTATE" in uin or "JOIN #" in uin or "tmi.twitch.tv 353" in uin or "tmi.twitch.tv 366" in uin):
            info["message"] = "twitch info message"
            info["channel"] = ""
            info["sent-ts"] = ""
            info["user-id"] = ""
            info["@badges"] = ""
            info["display-name"] = "twitch"
            info["mod"] = "0"
            info["subscriber"] = "0"
            info["user-type"] = ""
        
        elif(uin.startswith("PING")):
            afk()
        
        elif(len(inputSplit) == 3):
            msgInit = inputSplit[2]
            message = msgInit.split("\r")[0]
            info["message"] = message

            chanInit = inputSplit[1]
            strSplit = chanInit.split(" ")
            chanTear = strSplit[2].split("#")
            channel = chanTear[1]
            info["channel"] = channel

        # Splits remaining tags into the dictionary so they can all be called.
        spcSplit = inputSplit[0].split(" ")
        tags = spcSplit[0].split(";")
        for i, t in enumerate(tags):
            obj = t.split("=")
            objTitle = obj[0]
            objValue = obj[1]
            info[objTitle] = objValue

            if(i >= len(tags) - 1):
                return info

    else:
        info = {} #This will be returned eventually.

        inputSplit = uin.split(" ") # Any input from the user will always give 5 objects, the rest are from twitch.

        info["message"] = "twitch info message"
        info["channel"] = ""
        info["sent-ts"] = ""
        info["user-id"] = ""
        info["@badges"] = ""
        info["display-name"] = "twitch"
        info["mod"] = "0"
        info["subscriber"] = "0"
        info["user-type"] = ""
        
        return info