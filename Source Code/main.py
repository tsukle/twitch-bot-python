import twpy

#------------------------------------------------------------------------------------------------
# Variables
client = twpy

#------------------------------------------------------------------------------------------------
# Chat and Command Center
rtndata = client.chat()
for data in rtndata: 
    if(data["message"] == "!command"):
        client.send("test")