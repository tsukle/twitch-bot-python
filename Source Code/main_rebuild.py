import events_rebuild
import os
import database
from colorama import init, Fore, Back, Style
from time import sleep

#------------------------------------------------------------------------------------------------
# Variables
client = events_rebuild
db = database

#------------------------------------------------------------------------------------------------
# Display Chat
rtndata = client.chat()
for data in rtndata: 
    print(Back.WHITE + Fore.BLACK + " " + data["display-name"] + " " + Style.RESET_ALL + " > " + data["message"])

    if(data["message"] == "!command"):
        client.send("test")