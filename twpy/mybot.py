import twpy

#------------------------------------------------------------------------------------------------
# Variables
client = twpy

#------------------------------------------------------------------------------------------------
# Chat and Command Center
rtndata = client.chat(#Set this to True if you want to use the in-built database.)
for data in rtndata: 
    if(data["message"] == "!command"):
        client.send("test")