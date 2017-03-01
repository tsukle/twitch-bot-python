import sqlite3

db = sqlite3.connect("database.db")
c = db.cursor()

#This creates the commands table if it does not exist
def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS Commands(command TEXT, response TEXT, level TEXT)")

#query adds command/response to the commands table
def addCommand(command, response, level):
    try:
        c.execute("INSERT INTO Commands (command, response, level) VALUES (?, ?, ?)", (command, response, level))
        db.commit()
        return 1
    except sqlite3.OperationalError as e:
        return e

#query removes command/response to the commands table
def removeCommand(command):
    try:
        c.execute("DELETE FROM Commands WHERE command=?", (command,))
        db.commit()
        return 1
    except sqlite3.OperationalError as e:
        return e

#query fetches response on request of a command
def getCommand(command):
    c.execute("SELECT * FROM Commands WHERE command = ?", (command,))
    response = c.fetchall()
    if response is not None:
        return response
    else:
        return 0

#query fetches list off all of the commands available
def getCommandList():
    x = "Commands: "
    c.execute("SELECT * FROM Commands")
    d = c.fetchall()
    if (d == None):
        return None
    else:
        for index, com in enumerate(d):
            command = com[0]
            level = com[2]
            if(index >= len(d) - 1):
                x = x + command + " - " + level
                return x
            else:
                x = x + command + " - " + level + "  |  "