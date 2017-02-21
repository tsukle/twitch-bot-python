import sqlite3

db = sqlite3.connect("database.db")
c = db.cursor()

#This creates the commands table if it does not exist
def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS Commands(command TEXT, response TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS Moderators(name TEXT)") # Store them for now, might use it, might not.

#query adds command/response to the commands table
def addCommand(com, response):
    try:
        c.execute("INSERT INTO Commands (command, response) VALUES (?, ?)", (com, response))
        db.commit()
        return 1
    except sqlite3.OperationalError as e:
        return e

#query removes command/response to the commands table
def removeCommand(dcom):
    try:
        c.execute("DELETE FROM Commands WHERE command=?", (dcom,))
        db.commit()
        return 1
    except sqlite3.OperationalError as e:
        return e

#query fetches response on request of a command
def getCommand(com):
    c.execute("SELECT * FROM Commands WHERE command = ?", (com,))
    response = c.fetchone()
    if response is not None:
        return response[1]
    else:
        return 0

#query fetches response on request of a command
def getCommandList():
    x = "Commands: "
    c.execute("SELECT command FROM Commands")
    d = c.fetchall()
    #enumerate d and add commands to the string until
    for index, com in enumerate(d):
        res = com[0]
        if(index >= len(d) - 1):
            x = x + res
            return x
        else:
            x = x + res + "  |  "