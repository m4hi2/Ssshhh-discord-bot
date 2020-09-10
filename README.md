# Ssshhh-discord-bot
My friends won't stop talking while playing "Among Us". Customizing and setting up big ass moderation bots were too much work for my tiny brain. So here it is.
This is a very basic bot. This just mutes everyone on a voice channel. I couldn't figure out how to hook to the game for automatically change the mute state when discussions
came up in Among Us game so had to go this route. In future I want to add voice commands, like "Jarvis, mute all" and "Jarvis, unmute all" but the ultimate solution
would be too interface with the game.



----
## How to invite the bot to your server? 
Use this invite [link](https://discord.com/api/oauth2/authorize?client_id=753424617485631561&permissions=282067984&scope=bot). But remember the bot server literary runs
on a Raspberry PI 3B in my home. So, I **highly** encourage you to run your own bot server. 

## How to use? 
The bot uses "." (dot) as command prefix. So, you can, 
- mute all users in a voice channel by `.mute` or `.m`
- unmute all users in a voice channel by `.unmute` or `.u`

**The voice channel join is there but the intended feature is yet to be implemented** 

## How to run your own bot server? 
        You need python 3.6 or higher to make this work. 

1. Follow [this](https://discordpy.readthedocs.io/en/latest/discord.html) to create a bot. 
2. Select the following permission for step 6 in the link: 
  - Manage Channels
  - View Channels
  - Connect
  - Mute Members
  
3. Clone this repo with `git clone https://github.com/m4hi2/Ssshhh-discord-bot.git`
4. Install the requirements with `pip install -r requirements.txt`
5. Create a `.env` file with `DISCORD_TOKEN='YOUR BOT TOKEN'` in the file. (You got this TOKEN when creating the bot. Check the link in step 1.)
7. Run the bot with `python3 bot.py`
8. Invite the bot to your desired server and enjoy it!

## Want to contribute? 
Open an issue or send a pull request. EZ. 
