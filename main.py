import openai
from discord.ext import commands
import discord

# OpenAI API KEY
openai.api_key = open_ai_token #replace with your open ai token
# Discord app token
discord_token = discord_bot_token #replace with your discord bot token

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.command()
async def ask(ctx, *args):
    message = ""
    for i in args:
        message += i + " "
    # print(message)
    await ctx.send(f"Generuję odpowiedź...")
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{message[:-1]}",
            max_tokens=4050,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        await ctx.send(f"<@{ctx.message.author.id}> {response}")
    except Exception as e:
        await ctx.send(f"Wystąpił błąd. Spróbuj jeszcze raz")
        print(e)
bot.run(discord_token)


