import events
import events_rebuild
import os
import database
from time import sleep
from colorama import init, Fore, Back, Style

init(autoreset=True)
os.system("mode con cols=120 lines=50")

#Initial Setup | Configures the socket creation and loads chat in console.
bot = events
bot2 = events_rebuild
bot.setup()
botSocket = bot.createSocket()

db = database
db.createTable()

readBuffer = "".encode()


#Loops program to keep bot running and prints a source of the chat
while True:
    readBuffer = botSocket.recv(1024)
    readBuffer = readBuffer.decode()
    msg = readBuffer.split("\n")
    readBuffer = readBuffer.encode()
    readBuffer = msg.pop()

    for line in msg:
        #Returns user and message without commands
        username = bot.getUser(line)
        message = bot.getMessage(line)
        message = str(message)
        print(line)
        bot2.info(line)

        ############################################################################################
        ######COMMENTED OUT SO I CAN SEE WHAT THE NEW RESPONSES ARE TO FIND USERSTATE ETC...########
        ############################################################################################

        #Message replacements to make the console look lit af :)
        # if(username == "twitch" and message.startswith("x5edtxmWKw")):
        #     print("____________________________________________________")
        #     print(Fore.BLACK + Back.CYAN + " INFO " + Style.RESET_ALL + " > " + "Now displaying the chat.")
        #     bot.sendSpecialMessage("has joined the chat.")

        # elif(username == "bot" and message.startswith("x5edtxmWKwx5ed")):
        #     g = 1

        # elif(username == "bot"):
        #     print(Fore.BLACK + Back.YELLOW + " BOT " + Style.RESET_ALL + "->   " + message)

        # elif(username == "twitch" and message.startswith("Welcome, GLHF!")):
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "Connecting to the Twitch IRC with: " + Back.YELLOW + Fore.BLACK + " BOT " + Style.RESET_ALL)
        #     sleep(0.5)

        # elif(username == "twitch" and message.startswith("Your host is tmi.twitch.tv")):
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "Host: " + Fore.LIGHTGREEN_EX + "irc.twitch.tv")
        #     sleep(0.2)
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "Port: " + Fore.LIGHTGREEN_EX + "6667")
        #     sleep(0.2)
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "Channel: " + Fore.LIGHTGREEN_EX + str(bot.settings["channel"]))
        #     sleep(0.2)

        # elif(username == "twitch" and message.startswith("This server is rather new") or message.startswith("tsuklebot") or message.startswith("None") or message.startswith("-") or message.startswith("You are in a maze of twisty passages, all alike.")):
        #     g = 0
        
        # elif(username == "twitch" and message.startswith(">")):
        #     h = 0
        #     x = True
        #     o = "."
        #     z = "Loading Database"
        #     while x == True:
        #         print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + z, end="")
        #         sleep(0.4)
        #         print(o, end="")
        #         sleep(0.4)
        #         print(o, end="")
        #         sleep(0.4)
        #         print(o, end="")
        #         sleep(0.4)
        #         print(o, end="")
        #         sleep(0.4)
        #         print(o, end="")
        #         sleep(0.4)
        #         print("")
        #         x = False
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "Database Loaded.")
        #     sleep(0.3)
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "IRC client succesfully connected.")
        #     sleep(0.3)
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + "Loading bot into chat.")
        #     sleep(0.3)

        # elif(username == "twitch"):
        #     print(Fore.WHITE + Back.MAGENTA + " TWITCH " + Style.RESET_ALL + "   " + message)

        # else:
        #     print(Fore.BLACK + Back.WHITE + " " + username.upper() + " " + Style.RESET_ALL + " > " + message)



            
        #------------------------------------------------------------------------------------------------------
        #Command check
        if(message.startswith("!") and "addcom" in message and username == str(bot.settings["channel"])):
            bot.createCommand(message)

        elif(message.startswith("!") and "delcom" in message and username == str(bot.settings["channel"])):
            bot.deleteCommand(message)
        
        elif(message.startswith("!") and "commands" in message):
            cmdRes = db.getCommandList()
            bot.sendMessage(cmdRes)

        elif(message.startswith("!")):
            bot.execCommand(message)
        #------------------------------------------------------------------------------------------------------

        

