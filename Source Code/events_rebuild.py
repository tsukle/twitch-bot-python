import socket
import json
import database
from colorama import init, Fore, Back, Style
from time import sleep

#------------------------------------------------------------------------------------------------
# Initial Settings
init(autoreset=True)

#------------------------------------------------------------------------------------------------
# Variables
s = socket.socket()

#------------------------------------------------------------------------------------------------
# Open JSON settings file
with open("settings_personal.json") as data:
    opt = json.load(data)


#------------------------------------------------------------------------------------------------
# Create an IRC connection
def connect():
    s.connect(("irc.twitch.tv", 6667))
    s.send(("CAP REQ :twitch.tv/membership\r\n").encode())
    s.send(("CAP REQ :twitch.tv/commands\r\n").encode())
    s.send(("CAP REQ :twitch.tv/tags\r\n").encode())
    s.send(("PASS " + opt["authkey"] + "\r\n").encode())
    s.send(("NICK " + opt["username"] + "\r\n").encode())
    s.send(("JOIN #" + opt["channel"] + "\r\n").encode())
    return s

#------------------------------------------------------------------------------------------------
# Bot events
def send(message, s = None): # Send a chat message (if s is true, the message with append /me)
    if(s is None):
        construct = "PRIVMSG #" + opt["channel"] + " :" + message + "\r\n"
        s.send((construct).encode())
        print("Sent > " + message)
        sleep(1.5)
    else:
        construct = "PRIVMSG #" + opt["channel"] + " :/me " + message + "\r\n"
        s.send((construct).encode())
        print("Sent > " + message)
        sleep(1.5)

def afk():
    construct = "PONG :tmi.twitch.tv\r\n"
    s.send((construct).encode())
    print("AFK Check Complete.")

def info(string):
    tags = string.split(";")
    x = "##### => "
    for i, t in enumerate(tags):
        tag = t
        if(i >= len(tags) - 1):
            x = x + tag
            print("")
            print("")
            print(x)
        else:
            x = x + tag + "  |  "
            ####SPLICE THE "=" AND CREATE A NEW ARRAY, APPEND IT ALL.
