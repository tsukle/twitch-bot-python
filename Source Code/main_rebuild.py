import events_rebuild
import os
from colorama import init, Fore, Back, Style
from time import sleep

#------------------------------------------------------------------------------------------------
# Variables
client = events_rebuild

#------------------------------------------------------------------------------------------------
# Display Chat
rtndata = client.chat()
for data in rtndata: 
    if(data["message"] == "!command"):
        client.send("test")