import numpy
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = "INSERT-TOKEN-HERE"

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("."), intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is about to get racist")

@bot.command()
async def sup(channel):

    trashboat_quotes = open("trashboat_msgs.txt", encoding="utf8").read()

    single_words = trashboat_quotes.split()

    def make_pairs(single_words):
        for i in range(len(single_words)-1):
            yield (single_words[i], single_words[i+1])

    pairs = make_pairs(single_words)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)

        else:
            word_dict[word_1] = [word_2]

    first_word = numpy.random.choice(single_words)

    chain = [first_word]

    num_of_words = random.randrange(6, 20)

    for i in range(num_of_words):
            chain.append(numpy.random.choice(word_dict[chain[-1]]))

    " ".join(chain)

    await channel.send(chain)

bot.run(TOKEN)
