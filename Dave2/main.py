from keep_alive import keep_alive
from discord.ext import commands
import os
import random
import asyncio
import discord


client = commands.Bot(command_prefix = '!')



insults = [
  "Kill yourself, you fat fucking slob, piece of shit bass fisher",
  "You're the reason me and mom divorced",
  "Thats it im gettin the switch",
  "I will put you down just like I did that piece of shit dog",
  "How many times do i have to tell you how usless of a fisherman you are?",
  "This is Biden's America",
  "Nigger",
  "Jew",
  "Beaner",
  "Terrorist", 
  "Fucker",
  "You fucking pile of garbage, I wish your peice of shit mom aborted you",
  "You are no longer a use to the communist party, please face the wall"
]

gold = [
  "a Boot! Oh hey, thats where my boot went!",
  "a Devil's Hole Pupfish! WOW THIS IS THE RAREST FISH IN THE WORLD!",
  "Kevin's Sword! Wait, THIS IS ONE OF THE RAREST ITEMS IN THE DISCORD SERVER!",
  "a Shark! HOLY SHIT YOU CAUGHT A SHARK!"
]

purple = [
  "Heroin Needle",
  "Tigerfish"
]

blue = [
  "an Eel",
  "a Clownfish",
]

green = [
  "Swordfish",
  "Bass",
  "Salmon"
]

gray = [
  "Carp",
  "Shrimp",
  "Tuna",
  "Goldfish",
  "Pufferfish",
]

compliments = [
  "That was some fine fishing son! :)",
  "Thats one fine something you caught there! <3",
  "Im proud of you son! Great Fishing!",
  "Im taking you to Bass Pro Shop after therapy!",
  "Your Mom never understood me, but it looks like you get it!",
  "That was so great! I promise I wont beat you for about a week!",
  "I'll drink to that!"
]




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  available = True

  if random.randint(0,4) == 0 and available == True:
    available = False
    await message.channel.send("Someone spotted something in the river! Use !catch to try to catch it!")

    try:
      sendM = await client.wait_for('message', check=lambda m: m.channel == message.channel, timeout = 5.0)

    except asyncio.TimeoutError:
      await message.channel.send("You took too long to react, you'll get it next time!")

    else:
      if sendM.content.lower() == "!catch":
        #50% chance
        catchChance = random.randint(0, 2)
        if catchChance == 0:
          #1-100
          rarity = random.randint(1, 100)

          if rarity <= 70: #Less than or equal to 70 you get a basic fish
            await message.channel.send(f"You caught a {random.choice(gray)}! Not that good but we all start somewhere!\n{random.choice(compliments)}")
            available = True

          elif rarity > 70 and rarity >= 85:
            await message.channel.send(f"You caught a {random.choice(green)}! Now we're talking!\n{random.choice(compliments)}")
            available = True

          elif rarity > 85 and rarity >= 95:
            await message.channel.send(f"You caught {random.choice(blue)}! Wow, even I couldn't catch this!\n{random.choice(compliments)}")
            available = True

          elif rarity > 95 and rarity >= 99:
            await message.channel.send(f"You caught a {random.choice(purple)}!This is great! Don't worry I'll take this for safe keeping!\n{random.choice(compliments)}")
            available = True
          
          elif rarity == 100: #1% chance
            await message.channel.send(f"You caught {random.choice(gold)}\n{random.choice(compliments)}")
            available = True

        else:
          await message.channel.send(f"You didn't catch whatever was in the river\n{random.choice(insults)}")
          available = True

  await client.process_commands(message)

@client.command()
async def join(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()
  await ctx.voice_client.play(discord.FFmpegPCMAudio(source=r"morioh.mp3"))

@client.command()
async def play(ctx):
  await ctx.voice_client.play(discord.FFmpegPCMAudio(source=r"morioh.mp3"))

@client.command()
async def play1h(ctx):
  await ctx.voice_client.play(discord.FFmpegPCMAudio(source=r"morioh1h.mp3"))

@client.command()
async def leave(ctx):
  await ctx.voice_client.disconnect()

@client.command()
async def fishinglessons(ctx):
  await ctx.send(f'Commands {ctx.message.author.mention}:\nFishing: !fish\nFishing gives a 50/50 chance to catch a fish')

@client.command()
async def fish(ctx):
  fishing = random.randint(0, 1)
  if fishing == 0:
    await ctx.send("You Didn't Catch the Fish")
    await ctx.send(f'{random.choice(insults)} {ctx.message.author.mention}')
  else:
    await ctx.send("You Caught the Fish!")
    await ctx.send(f'{random.choice(compliments)} {ctx.message.author.mention}')

@client.event
async def on_voice_state_update(member, before, after):
  if before.channel is None or after.channel is not None:
    vc = await member.voice.channel.connect()
    vc.play(discord.FFmpegPCMAudio(source=r"morioh.mp3"))

keep_alive()
client.run(os.getenv('TOKEN'))