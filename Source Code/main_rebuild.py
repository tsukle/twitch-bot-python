import events_rebuild

#------------------------------------------------------------------------------------------------
# Variables
client = events_rebuild

#------------------------------------------------------------------------------------------------
# Chat and Command Center
rtndata = client.chat()
for data in rtndata: 
    if(data["message"] == "!command"):
        client.send("test")