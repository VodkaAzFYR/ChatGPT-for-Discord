import openai
from discord.ext import commands
import discord

# OpenAI API KEY
openai.api_key = ''
# Discord app token
discord_token = ''

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.command()
async def ask(ctx, *args):
    message = ""
    for i in args:
        message += i + " "
    # print(message)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{message[:-1]}",
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    await ctx.send(f"<@{ctx.message.author.id}> {response}")

bot.run(discord_token)


