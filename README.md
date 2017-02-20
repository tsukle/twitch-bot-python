# ![Twitch Logo](http://www.twitch.tv/favicon.ico "Twitch Logo") Twitch Chat Bot ![Twitch Logo](http://www.twitch.tv/favicon.ico "Twitch Logo")
A Twitch Chat Bot created with Python and SQlite3  

This project is not complete but it is at a basic and working state, I will be adding as much as I can to this bot and cleaning up the code in order to make it as powerful and as useful as I can.

------

## - Folders ![WutFace](https://static-cdn.jtvnw.net/emoticons/v1/28087/1.0 "WutFace")
There are two folders in this repository:
* *builds*
* *source code*

The reason there are two folders is pretty simple, for anyone that wants a bot that is built and ready to be used,
they can download the contents of the Builds folder which has all you need to run the bot in your chat.
For anyone that wants to add/change the bot in any way, they can pull or download the Source Code folder which consists
of 4 files:
* *database.py*
* *events.py*
* *main.py*
* *settings.json*

------

##  - Starting The Bot ![PogChamp](https://static-cdn.jtvnw.net/emoticons/v1/88/1.0 "PogChamp")
The built bot is very simple to run. Upon downloading the folder and placing it somewhere on your PC,
 you will find a bunch of files, the one you need to focus on is:
 >`settings.json`

This file is where you need to feed in your bot accounts:
 * *Bot Account Username*
 * *OAuth Key (Get it [here](https://twitchapps.com/tmi/))*
 * *Channel Name*

The finished product should look something like this:
 ```javascript
{
    "username": "tsuklebot",
    "authkey": "oauth:...",
    "channel": "tsukle"
}
```

Once you have done this, save the file and open the bot.exe file in the folder. Voila!

------

## - Using The Bot ![CoolStoryBob](https://static-cdn.jtvnw.net/emoticons/v1/123171/1.0 "CoolStoryBob")
Now that you have the bot up and running. Here are the basics to controlling it and adding commands.  
>Channel Owner Commands:

* *`!addcom` - Adds a command to the database.*
    * *Usage: !addcom [command] [response]*
    * *Example: !addcom !test this is a test command.*
* *`!delcom` - Removes a command from the database.*
    * *Usage: !delcom [command]*
    * *Example: !delcom !test*

>Typical Commands:

* *`!commands` - Lists all of the commands currently in the database.*
    * *Usage: !commands*

The bot runs in a console window which you should have noticed by now. You will see messages from the chat and bot in it.
You will also see messages come up from `INFO` this is just a notification for you and it will not show up in your twitch chat.  
An example of an `INFO` message:
>`INFO > Now displaying the chat.`

These messages will alert you when you have successfully added or removed a command and when an `*AFK check` has been done.  
>`* An AFK check is done every 5-10 minutes by Twitch, the bot will automatically respond to Twitch's AFK check in order to 
 keep the bot connected to the chat, you will get a notification in your console when a check has been completed.`

 That is pretty much it, you are now up and running. Add any commands you want, delete any commands you want. Enjoy.

 ------

## - Programmers ![Kappa](https://static-cdn.jtvnw.net/emoticons/v1/25/1.0 "Kappa")
If you want to mess with the source code I recommend you use [Python 3.5](https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe)
or onwards. The code was compiled and built using [PyInstaller](http://www.pyinstaller.org/), if you wish to do the same with your
changed code then do not use [Python 3.6](https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe) as it is not yet supported, 
use [3.5](https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe).

The program also uses a module called [Colorama](https://pypi.python.org/pypi/colorama) for the console 
colors which you may need to install yourself depending on the version of Python you have, if it throws an error about colorama when 
running the bot, it most likely means you need to install it.

To start the bot, run:
>`main.py`

Enjoy hacking around with the code!

------
## - Me ![Tsukle Logo](https://tsukle.com/favicons/favicon-32x32.png)
Just incase you want to see more of me:
* [Website](https://tsukle.com)
* [Twitter](https://twitter.com/tsukle)
* [Twitch](https://twitch.tv/tsukle)
* [Dribbble](https://dribbble.com/tsukle)
* [Join our community on Discord](https://discord.gg/aeAHmte)



