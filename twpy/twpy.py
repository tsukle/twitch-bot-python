import socket
import json
import database
from colorama import init, Fore, Back, Style # Module imported
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
with open("settings.json") as data:
    opt = json.load(data)

#------------------------------------------------------------------------------------------------
#Initial Prints non DB
def initNoDB():
    print("""
twpy v1.0.3
https://twpy.uk
Thank you for using twpy.
    """)

#------------------------------------------------------------------------------------------------
#Initial Prints with DB
def initDB():
    print("""
twpy v1.0.3
https://twpy.uk
Thank you for using twpy.
_____________________________________________________            
!addcom level !command response - for adding commands
!delcom !command - for removing commands
!commands - for listing commands
_____________________________________________________
    """)

#------------------------------------------------------------------------------------------------
# Create an IRC connection
def connect():
    init()
    s.connect(("irc.twitch.tv", 6667))
    s.send(("CAP REQ :twitch.tv/membership\r\n").encode())
    s.send(("CAP REQ :twitch.tv/commands\r\n").encode())
    s.send(("CAP REQ :twitch.tv/tags\r\n").encode())
    s.send(("PASS " + opt["authkey"] + "\r\n").encode())
    s.send(("NICK " + opt["username"] + "\r\n").encode())
    s.send(("JOIN #" + opt["channel"] + "\r\n").encode())
    return s

#------------------------------------------------------------------------------------------------
# Chat
def chat(setCommands = None):
    display = "".encode()
    con = connect()
    if(setCommands == None):
        initNoDB()
    else:
        initDB()
    while True:
        display = con.recv(1024)
        display = display.decode()
        message = display.split("\n")
        display = display.encode()
        display = message.pop()

        for line in message:
            response = info(line)
            # We do not want to return this data as it is an IRC message from Twitch or JTV.
            if(response["display-name"] == "twitch" or response["display-name"].lower() == opt["username"]):
                dontDoAnything = 1

            # This is a command (Do something with it.).
            elif(response["message"].startswith("!addcom") and setCommands == True):
                if(response["user-type"] == "mod"):
                    print(Back.WHITE + Fore.BLACK + " " + response["display-name"].upper() + " " + Style.RESET_ALL + " > " + response["message"])
                    spliced = response["message"].split(" ", 3) #Split it 3 times ("!addcom", "user-level", "!command", "response")
                    level = spliced[1]
                    command = spliced[2]
                    response = spliced[3]

                    # Don't allow hard-coded commands to be added
                    
                    if(command == "!addcom" or command == "!delcom" or command == "!commands"):
                        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Is a reserved command.")

                    # Allow any other commands
                    else:
                        returned = db.addCommand(command, response, level)
                        if (returned != 0):
                            print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Added to the database.")
                        
                        else:
                            print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Error: " + str(returned))
                else:
                    print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > User: " + response["display-name"] + " - Does not have permission to use this command.")
            
            # This is a command (Do something with it.).
            elif(response["message"].startswith("!delcom") and setCommands == True):
                if(response["user-type"] == "mod"): 
                    print(Back.WHITE + Fore.BLACK + " " + response["display-name"].upper() + " " + Style.RESET_ALL + " > " + response["message"])
                    spliced = response["message"].split(" ", 1)
                    pre = spliced[1]
                    post = pre.split("\r")
                    command = post[0]
                    returned = db.removeCommand(command)
                    if (returned == 1):
                        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Removed from the database.")
                    else:
                        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Error: " + str(returned))
                else:
                    print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > User: " + response["display-name"] + " - Does not have permission to use this command.")

            elif(response["message"] == "!commands"  and setCommands == True):
                print(Back.WHITE + Fore.BLACK + " " + response["display-name"].upper() + " " + Style.RESET_ALL + " > " + response["message"])
                returned = db.getCommandList()
                if(returned == None):
                    send("There are currently no commands set for this channel.")
                else:
                    send(returned)

            # This is a command (Do something with it.).
            elif(response["message"].startswith("!")  and setCommands == True):
                print(Back.WHITE + Fore.BLACK + " " + response["display-name"].upper() + " " + Style.RESET_ALL + " > " + response["message"])
                spliced = response["message"].split("\r")
                command = spliced[0]
                returned = db.getCommand(command)
                if(returned == []):
                    print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > Command: " + command + " - Not found in the database.")
                elif(returned != [] and response["user-type"] != returned[0][2]):
                    if(response["user-type"] == "mod"):
                        send(returned[0][1])
                    else:
                        print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > User: " + response["display-name"] + " - Does not have permission to use this command.")
                else:
                    send(returned[0][1])

            # We want to return this good stuff.
            else:
                print(Back.WHITE + Fore.BLACK + " " + response["display-name"].upper() + " " + Style.RESET_ALL + " > " + response["message"])
                yield response

#------------------------------------------------------------------------------------------------
# Bot events
def send(message, sp = None): # Send a chat message (if s is true, the message will append /me)
    if(sp is None):
        construct = "PRIVMSG #" + opt["channel"] + " :" + message + "\r\n"
        s.send((construct).encode())
        print(Back.YELLOW + Fore.BLACK + " BOT " + Style.RESET_ALL + " > " + message)
        sleep(1.5)
    else:
        construct = "PRIVMSG #" + opt["channel"] + " :/me " + message + "\r\n"
        s.send((construct).encode())
        print(Back.YELLOW + Fore.BLACK + " BOT " + Style.RESET_ALL + " > " + message)
        sleep(1.5)

def afk(): # This responds to Twitch's afk PING requests.
    construct = "PONG :tmi.twitch.tv\r\n"
    s.send((construct).encode())


#------------------------------------------------------------------------------------------------
# Message information, returns attributes.
def info(uin):
    if(uin.startswith("@badges")):
        info = {} #This will be returned eventually.

        inputSplit = uin.split(":")

        #This is a check to stop these messages from being sent to chat.
        if(":jtv MODE" in uin or "GLOBALUSERSTATE" in uin or "USERSTATE" in uin or "ROOMSTATE" in uin or "JOIN #" in uin or "tmi.twitch.tv 353" in uin or "tmi.twitch.tv 366" in uin):
            info["display-name"] = "twitch"
        
        elif(uin.startswith("PING")):
            afk()
        
        # Gets the message sent and the channel it was sent from.
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
                if(info["user-type"] == ""):
                    info["user-type"] = "all"
                    return info
                else:
                    return info

    else:
        info = {} #This gets returned.
        # Returns the display-name twitch as all of the messages are from the IRC connection. Dealt with later.
        inputSplit = uin.split(" ")

        info["message"] = ""
        info["channel"] = ""
        info["sent-ts"] = ""
        info["user-id"] = ""
        info["@badges"] = ""
        info["display-name"] = "twitch"
        info["mod"] = "0"
        info["subscriber"] = "0"
        info["user-type"] = ""
        
        return info