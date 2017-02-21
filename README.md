# ![Twitch Logo](http://www.twitch.tv/favicon.ico "Twitch Logo") Twitch Chat Bot ![Twitch Logo](http://www.twitch.tv/favicon.ico "Twitch Logo")
A Twitch Chat Bot created with Python and SQlite3  

This project is not complete but it is at a basic and working state, I will be adding as much as I can to this bot and cleaning up the code in order to make it as powerful and as useful as I can.

------

## - Users
This branch is dedicated to pulling extra tags from the IRC messages in order to give each user an array attribute which will hold values
such as `user-type` and `username` which can be used for command management and chat control.


Current plans with this branch:  
* *Make user an array holding attributing tags*
* *Give commands usage groups.*
    - *!addcom !test !owner|moderator|everyone| [response]*
* *Let moderators add commands (if the channel owner chooses to allow it)*
