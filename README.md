# TrashBot
A Discord Python Bot, Generating And Sending Messages Using Markov Chains.

This is a Discord bot written in python3.10.6, that uses a markov chain and a list of sentences to generate realistic and believable.

To use the Bot, you'll need to replace the following line with your own Bot token:


TOKEN = "INSERT-TOKEN-HERE"


You should also consider editing the script to use your own sentence dictionary. you can do this by making the following edits:


trashboat_quotes = open("trashboat_msgs.txt", encoding="utf8").read() -> trashboat_quotes = open("YOUR_TXT_FILE_GOES_HERE", encoding="utf8").read()


I would recommend using a list with more than 400 sentences for basic functionality.

Have fun :D
