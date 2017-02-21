import twitchpy

#------------------------------------------------------------------------------------------------
# Variables
client = twitchpy

#------------------------------------------------------------------------------------------------
# Chat and Command Center
rtndata = client.chat()
for data in rtndata: 
    if(data["message"] == "!command"):
        client.send("test")