# ![Twitch Logo](http://www.twitch.tv/favicon.ico "Twitch Logo") Twitch Chat Bot ![Twitch Logo](http://www.twitch.tv/favicon.ico "Twitch Logo")
A Twitch Chat Bot created with Python and SQlite3  

This project is not complete but it is at a basic and working state, I will be adding as much as I can to this bot and cleaning up the code in order to make it as powerful and as useful as I can.

------

## - Users
This branch is dedicated to pulling extra tags from the IRC messages in order to give each user an array attribute which will hold values
such as `user-type` and `username` which can be used for command management and chat control.


Current plans with this branch:  
* *~~Make user an array holding attributing tags~~* ==> **Complete.**
* *Give commands usage groups.* ==> **Up next.**
    - *!addcom !test !owner|moderator|everyone| [response]*
* *Let moderators add commands (if the channel owner chooses to allow it)*
* *Operation Code Cleanup* ==> **Working on it as I go along.**

------

## - Library
This branch also focuses on turning the bot script into a library that anyone can call in their script and use with minimalistic amounts of code.  
For example:
```python
    import twitchpy

    client = twitchpy

    returndata = client.chat()
    for data in returndata: 
        # If the message is "!command" and the user that sent it is a moderator, send "test" to the chat.
        if(data["message"] == "!command" and data["user-type"] == "mod"):
            client.send("test")
```

As seen above, all you need to actually make your own bot from my library is to call for the `chat` function from the twitchpy module and it will return all of the data that 
you need to create normal hard coded commands. The backend runs in a loop and yields data back rather than returning it so that the loop is not broken, this is why you use a for loop to go through the returned (yielded) data. 

Every new message that the bot receives from the chat is returned in the same way so that one `if` statement will run every new returned piece of data through it.

The `send` function has a 1.5 second sleep time after a message is sent to the chat to stop it from sending too many messages at once since this can result in an 8 hour global chat ban to your associated account.

------

## - What is returned?
You may want to know what is actually returned to you for each message so you can create special features for your own bots.  
The return data from `client.chat()` is a dictionary (python's json) containing the following:  
```python
    'sent-ts': 'No idea, it is not documented anywhere', 
    'message': 'The message that they sent', 
    'user-id': 'Users ID', 
    'mod': 'Is the user a moderator (0/1)', 
    'emotes': 'Put the emote id in this link for the icon http://static-cdn.jtvnw.net/emoticons/v1/:emote_id/:3.0', 
    'id': 'This is a unique id for a message', 
    'display-name': 'Username of the person that sent the message', 
    'color': 'Their username colour in chat', 
    '@badges': 'Can have a staff, admin, global_mod, moderator, subscriber and turbo badge (I have not parsed this so dont use it.)', 
    'user-type': 'What type of user is it? (mod, admin, global-mod or staff)', 
    'channel': 'The channel the message was sent from', 
    'room-id': 'ID of the channel', 
    'tmi-sent-ts': 'No idea, it is not documented anywhere', 
    'subscriber': 'Is this person a subscriber of the channel (0/1)', 
    'turbo': 'Is this a turbo user, this wont work with twitch prime members. (0/1)'
```

To use any of the above dictionary objects in your bot you just call `data["name-of-object"]`.  
For example:  
```
    data["mod"]    <== This will either return a 1 or 0 depending on if they are a moderator.
```

You shouldn't be short of returned data to mess with.
