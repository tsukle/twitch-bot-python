import twpy

#------------------------------------------------------------------------------------------------
# Variables
client = twpy

#------------------------------------------------------------------------------------------------
# Chat and Command Center
rtndata = client.chat(True, "has joined the channel")
for data in rtndata:
    doNothing = True