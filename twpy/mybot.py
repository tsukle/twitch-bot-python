import twpy

#------------------------------------------------------------------------------------------------
# Variables
client = twpy

#------------------------------------------------------------------------------------------------
# Chat and Command Center
rtndata = client.chat(True)
for data in rtndata:
    doNothing = 1
