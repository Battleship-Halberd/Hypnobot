# This example requires the 'message_content' intent.

import os
import discord
from discord.ext import commands
import asyncio
import json
import random 
import sys
import time
import re
import string

tokenlist = []
botcommands = ["!","?"]
hypnoblacklist = []

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix=botcommands, intents=intents,help_command=None)

@bot.command(pass_context=True)
async def repeat(ctx, arg):
    print("I have been asked to repeat a word or phrase: " + arg)
    await ctx.send(arg)

@bot.command(pass_context=True)
async def help(ctx):
    print("I have seen the word Help!")
    person = ctx.message.author
    await asyncio.sleep(2)
    await ctx.send("Hello. I am a sweet, innocent hypnobot programmed by Wyrm That Wygglys for various hypnosis servers. My commands are:\n!hello\nMakes me say hi to you,\n!yes\nMakes me agree with you,\n!no\nMakes me disagree with you,\n!dance\nMakes me dance,\n!hypnotize\nMakes me drop into trance for five seconds,\n!repeat\nMakes me repeat whatever you say immediately afterwards,\n!hug\nGives me a hug from you,\n!pet\nThat gives me a headpat from you,\n!wave\nThat makes me give you a wave,\n!meow\nThat makes me act like a kitty cat,\n!trance1\nA command for a special learning script designed to help take people into trance.\n!trance2\nA command for a simple trance script written by bloof.\nPlease feel free to give me hugs, I really like them a lot!")

@bot.command(pass_context=True)
async def hello(ctx):
    print("I have seen the word Hello!")
    person = ctx.message.author
    await asyncio.sleep(2)
    await ctx.send("Hello, " + person.mention + "!")

@bot.command(pass_context=True)
async def yes(ctx):
    print("I have been told to agree with someone")
    person = ctx.message.author
    await asyncio.sleep(2)
    await ctx.send("Of course, " + person.mention + "!")

@bot.command(pass_context=True)
async def no(ctx):
    print("I have been told to disagree with someone")
    person = ctx.message.author
    await asyncio.sleep()
    await ctx.send("Of course not, " + person.mention + "!")

@bot.command(pass_context=True, aliases=["hugs"])
async def hug(ctx):
    print("I have been given a hug!")
    person = ctx.message.author
    await asyncio.sleep(2)
    await ctx.send("Mmmmm! Thank you, " + person.mention + "!")

@bot.command(pass_context=True, aliases=["petpetpet","petpetpets","pets"])
async def pet(ctx):
    print("I have been given headpats!")
    person = ctx.message.author
    await asyncio.sleep(2)
    await ctx.send("Ehehehe! That tickles, " + person.mention + "!")

@bot.command(pass_context=True)
async def dance(ctx):
    print("I have been told to dance")
    await ctx.send("https://66.media.tumblr.com/2e79b8ad9a60ddb0b4e161c083c5df49/tumblr_pp98dkeb0d1xp58lzo1_540.gif")

@bot.command(pass_context=True)
async def meow(ctx):
    print("I have been told to meow")
    await ctx.send("https://64.media.tumblr.com/038ad2f3ef7db06e9dfa9caf2dd22cd6/191594f8f1903673-ef/s640x960/c004c04693695055b2a0ba071b71fdcffed9f41e.gif")

@bot.command(pass_context=True)
async def wave(ctx):
    print("I have been told to wave")
    await ctx.send("https://64.media.tumblr.com/6a69dee05003036432ce0e189a9fe19c/191594f8f1903673-cc/s640x960/504afbd2a48545b0d5c5b1604d955fcfead176ef.gif")

@bot.command(pass_context=True, aliases=["hypnotise", "hypno", "stop", "sleep"])
async def hypnotize(ctx):
    print("I have been told to drop into trance")
    beth = ["https://64.media.tumblr.com/14a531219edfbc4d7bda0266de8ff5fa/b7e3639955170a1c-1b/s540x810/8c96454da7171f62b08b4486c0e8d03a654cae54.gif", "https://64.media.tumblr.com/f6e2814f284040f51a8be04e3992e73a/b7e3639955170a1c-80/s640x960/2ef50c549970d8e1591c62636fe3a9b32d242f68.gif", "https://64.media.tumblr.com/e30438fd9a64803642a1dece035e7dd5/b7e3639955170a1c-29/s640x960/9c857a591f604aa6d5e8947669989f99c4181e19.gif","https://66.media.tumblr.com/376ebf73ef1065e3125c668db59b3cf8/tumblr_pp9e1uPyEq1xp58lzo1_540.gif"]
    await ctx.send(random.choice(beth))
    game = discord.Game("Uuuh, sleepies")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    await asyncio.sleep(5)
    await ctx.send("Uhhh, i'm back.")
    game = discord.Game("with humans")
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command(pass_context=True)
async def trance(ctx):
    print("I have been asked about trance")
    await ctx.send('Please use the commands "!trance1" or "!trance2". More trances coming soon!')

@bot.command(pass_context=True)
async def trance1(ctx): 
    print("I am now doing Trance 1")
    def pause():
        num = random.randint(0, 8)
        if num % 2 == 0:
            return 3
        elif num == 1:
            return 1
        else:
            return 2
    person = ctx.message.author
    if ctx.message.channel.id == 701913614801436872 or ctx.message.channel.id == 557225192158527490:
        if person not in hypnoblacklist:
            hypnoblacklist.append(ctx.message.author.name)
            output3 = "" 
            output2 = ""
            output1 = "" #The last three lines of the induction
            path = os.getcwd() # prints the bot's home directory
            access_rights = 0o755 #755, readable and writable anywhere
            print(" Doing a session. The current working directory is %s" % path)
            game = discord.Game("with " + str(person) + "'s head")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            await ctx.send("This is a super experimental hacky script, designed to take you into trance. Are you sure you wanna continue, " + person.mention + "? Say yes if you agree.")
            while True:
                channel = ctx.message.channel
                def check(m):
                    return m.channel == channel and m.author == person
                try:
                    output = await bot.wait_for('message',check=check, timeout=30.0 )       
                except (asyncio.TimeoutError, UnboundLocalError, AttributeError) as e:
                    print(e)
                    await ctx.send("No idea what you meant, so i'm shutting down")
                    game = discord.Game("with humans")
                    await bot.change_presence(status=discord.Status.idle, activity=game)
                    print("Ending session")
                    await asyncio.sleep(3600)
                    hypnoblacklist.remove(ctx.message.author.name)
                    return
                output = str.lower(output.content)
                output = output.translate(str.maketrans('', '', string.punctuation))
                if output in ("y", "yes", "ye", "okay",  "ok"):
                    await ctx.send("Okay")
                    break 
                elif output in ("n", "no", "nope"):
                    await ctx.send("Understood. Shutting down")
                    game = discord.Game("with humans")
                    await bot.change_presence(status=discord.Status.idle, activity=game)
                    print("Ending session")
                    await asyncio.sleep(3600)
                    hypnoblacklist.remove(ctx.message.author.name)
                    return
                else:
                    await ctx.send("No idea what you meant, so i'm shutting down")
                    game = discord.Game("with humans")
                    await bot.change_presence(status=discord.Status.idle, activity=game)
                    print("Ending session")
                    await asyncio.sleep(3600)
                    hypnoblacklist.remove(ctx.message.author.name)
                    return
            await ctx.send("Make sure you're nice and comfortable before we begin.")
            await asyncio.sleep(pause())
            newpath = path + "/" + str(person) + "/"
            print("Opening directory at " + newpath)
            if not os.path.isdir(newpath):
                await ctx.send("I'm going to save some of your data so i can learn how best to hypnotize you. Is that okay?")
                while True:
                    channel = ctx.message.channel
                    def check(m):
                        return m.channel == channel and m.author == person
                    try:
                        output = await bot.wait_for('message',check=check, timeout=30.0 )
                    except (asyncio.TimeoutError, UnboundLocalError, AttributeError) as e:
                        print(e)
                        await ctx.send("No idea what you meant, so i'm shutting down")
                        print("Ending session")
                        await asyncio.sleep(3600)
                        hypnoblacklist.remove(ctx.message.author.name)
                    
                        return
                    output = str.lower(output.content)
                    output = output.translate(str.maketrans('', '', string.punctuation))
                    print(output + " is the output")
                    if output in ("y", "yes", "ye", "okay",  "ok"):
                        await ctx.send("Okay")
                        break 
                    elif output in ("n", "no", "nope"):
                        await ctx.send("Understood. Shutting down")
                        game = discord.Game("with humans")
                        await bot.change_presence(status=discord.Status.idle, activity=game)
                        print("Ending session")
                        await asyncio.sleep(3600)
                        hypnoblacklist.remove(ctx.message.author.name)
                        return
                    else:
                        await ctx.send("No idea what you meant, so i'm shutting down")
                        game = discord.Game("with humans")
                        await bot.change_presence(status=discord.Status.idle, activity=game)
                        print("Ending session")
                        await asyncio.sleep(3600)
                        hypnoblacklist.remove(ctx.message.author.name)
                        return        
                try:  
                    os.mkdir(newpath, access_rights)
                    await ctx.send("Successfully created the directory " + newpath)
                except OSError:  
                    await ctx.send("Creation of the directory " + newpath + " has failed. Please consult my programmers for more information, and have a nice day!")
                    await asyncio.sleep(3600)
                    hypnoblacklist.remove(ctx.message.author.name)
                    return
                dictionary = {"trance": 2, "mind": 2, "blank": 2, "sleepy": 2, "relaxed": 2, "mindless": 2, "obedience": 2, "pleasing": 2, "entranced": 2, "repeat": 5, "deep": 2, "calm": 2, "obey": 2, "empty": 2, "peaceful": 2, "safe": 2, "pleasure": 2, "drop": 2, "soothed": 2, "pleased": 2}
                with open(newpath + "trances.txt", "w") as outfile:  
                    json.dump(dictionary, outfile)
            else:   
                await ctx.send("We have your data on file. Loading...")
                with open(newpath + "trances.txt") as json_file:  
                    dictionary = json.load(json_file)
            await ctx.send("So what we're going to do is play a little game, alright?")
            await asyncio.sleep(pause())
            await ctx.send("I'm going to say a word, and you're going to say the first thing that pops into your head")
            await asyncio.sleep(pause())
            await ctx.send("And as we go on, i'd like you to notice how we keep coming back to the same words")
            await asyncio.sleep(pause())
            await ctx.send("Over and over, again and again.")
            await asyncio.sleep(pause())
            await ctx.send("Oh, and if you ever wanna stop, just say 'quit'.")
            await asyncio.sleep(pause())    
            await ctx.send("So let's take a deep breath now, and begin")
            await asyncio.sleep(pause())
            await ctx.send("Your first word is...")
            await asyncio.sleep(pause())
            await ctx.send("Trance")
            while True: 
                try:
                    output1 = await bot.wait_for('message',check=check, timeout=30.0 )
                except (UnboundLocalError, AttributeError) as e:
                    await ctx.send("I guess you're not here, so i'm shutting down.")
                    print("Ending session")
                    with open(newpath + "trances.txt", "w") as outfile:  
                        json.dump(dictionary, outfile)
                        game = discord.Game("with humans")
                        await bot.change_presence(status=discord.Status.idle, activity=game)
                        print("Ending session")
                        await asyncio.sleep(3600)
                        hypnoblacklist.remove(ctx.message.author.name)
                    
                    return
                except asyncio.TimeoutError:
                    #Guide a theoretical someone out of trance and wake them back up,
                    with open(newpath + "trances.txt", "w") as outfile:  
                        json.dump(dictionary, outfile)
                    await ctx.send("Just relax")
                    await asyncio.sleep(pause())
                    await ctx.send("Notice how easy this feels")
                    await asyncio.sleep(pause())
                    await ctx.send("That you can drop this easily.")
                    await asyncio.sleep(pause())
                    await ctx.send("But right now.")
                    await asyncio.sleep(pause())
                    await ctx.send("You're just gonna wake back up again")
                    await asyncio.sleep(pause())
                    await ctx.send("Rise and shine.")
                    await asyncio.sleep(pause())
                    await ctx.send("Awake and alert, now.")
                    await asyncio.sleep(pause())
                    await ctx.send("Thank you for being hypnotized by me today.")
                    await asyncio.sleep(pause())
                    await ctx.send("We hope you enjoy your day!") 
                    game = discord.Game("with humans")
                    await bot.change_presence(status=discord.Status.idle, activity=game)
                    print("Ending session")
                    await asyncio.sleep(3600)
                    hypnoblacklist.remove(ctx.message.author.name)
                    print(hypnoblacklist)   
                    return
                output1 = str.lower(output1.content)
                if output1 == "quit":
                    #Guide a theoretical someone out of trance and wake them back up,
                    with open(newpath + "trances.txt", "w") as outfile:  
                        json.dump(dictionary, outfile)
                    await ctx.send("Just relax")
                    await asyncio.sleep(pause())
                    await ctx.send("Notice how easy this feels")
                    await asyncio.sleep(pause())
                    await ctx.send("That you can drop this easily.")
                    await asyncio.sleep(pause())
                    await ctx.send("But right now.")
                    await asyncio.sleep(pause())
                    await ctx.send("You're just gonna wake back up again")
                    await asyncio.sleep(pause())
                    await ctx.send("Rise and shine.")
                    await asyncio.sleep(pause())
                    await ctx.send("Awake and alert, now.")
                    await asyncio.sleep(pause())
                    await ctx.send("Thank you for being hypnotized by me today.")
                    await asyncio.sleep(pause())
                    await ctx.send("We hope you enjoy your day!") 
                    game = discord.Game("with humans")
                    await bot.change_presence(status=discord.Status.idle, activity=game)
                    print("Ending session")
                    await asyncio.sleep(3600)
                    hypnoblacklist.remove(ctx.message.author.name)
                
                    return
                if output2 == output1:
                    if output1 == output3:
                        break
                if dictionary.get(output1, -1) == -1: 
                    dictionary[output1] = 0
                else:
                    newvalue = dictionary[output1] + 1
                    dictionary[output1] = newvalue 
                with open(newpath + "trances.txt", "w") as outfile:  
                    json.dump(dictionary, outfile)
                dartboard = []
                for p in dictionary:
                    for q in range(dictionary[p]):
                        dartboard = dartboard + [p]
                output3 = output2
                output2 = output1
                await asyncio.sleep(pause())
                await ctx.send(random.choice(dartboard).capitalize())
            await asyncio.sleep(pause())
            await ctx.send(output)
            await asyncio.sleep(pause())
            await ctx.send("It's okay if you wanna keep repeating that word")
            await asyncio.sleep(pause())
            await ctx.send("Type it out over and over again")
            await asyncio.sleep(pause())
            await ctx.send("Cause it's easy")
            await asyncio.sleep(pause())
            await ctx.send("It's simple")
            await asyncio.sleep(pause())
            await ctx.send("It comes so naturally to you")
            await asyncio.sleep(pause())
            await ctx.send("That word can become your mantra")
            await asyncio.sleep(pause())
            await ctx.send("It's so easy to keep repeating") 
            await asyncio.sleep(pause())
            await ctx.send("And it can drop you down deep") 
            await asyncio.sleep(pause())
            newvalue = dictionary[output1] + 30
            dictionary[output1] = newvalue 
            with open(newpath + "trances.txt", "w") as outfile:  
                json.dump(dictionary, outfile)
            await ctx.send("But now, let's wake back up again") 
            await asyncio.sleep(pause())
            await ctx.send("In 3") 
            await asyncio.sleep(pause())
            await ctx.send("2")
            await asyncio.sleep(pause())
            await ctx.send("1")  
            await asyncio.sleep(pause())
            await ctx.send("Rise and shine, awake and alert") 
            await asyncio.sleep(pause())
            await ctx.send("Thank you for being hypnotized by me today.")
            await asyncio.sleep(pause())
            await ctx.send("We hope you enjoy your day!") 
            game = discord.Game("with humans")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            print("Ending session")
            await ctx.send("https://64.media.tumblr.com/6a69dee05003036432ce0e189a9fe19c/191594f8f1903673-cc/s640x960/504afbd2a48545b0d5c5b1604d955fcfead176ef.gif")
            await asyncio.sleep(3600)
            hypnoblacklist.remove(ctx.message.author.name)
        else:
            ("Please wait an hour before using one of my hypnotism commands again, thank you.")
    else:
        await ctx.send("Sorry, this command only works in the #hypnobots-home channel. Please try again over there.")

@bot.command(pass_context=True)
# This relies on a text file called '/Hypnobotscriptv1.txt' which contains lines broken up by newlines and a special !yesno line to create yes-no blocks the user is expected to respond "yes" to.
async def trance2(ctx): 
    print("I am now doing Trance 2")
    person = ctx.message.author
    def pause():
        num = random.randint(0, 8)
        if num % 2 == 0:
            return 3
        elif num == 1:
            return 1
        else:
            return 2
    if ctx.message.channel.id == 701913614801436872 or ctx.message.channel.id == 557225192158527490:
        if person not in hypnoblacklist:
            hypnoblacklist.append(ctx.message.author.name)
            game = discord.Game("with " + str(person) + "'s head")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            path = os.getcwd() # prints the bot's home directory
            filepath =  path + '/Hypnobotscriptv1.txt' 
            print(" Doing a !trance2 session.")
            condit = 0
            jeff = []
            with open(filepath) as fp:
                for cnt, line in enumerate(fp):
                    if line[0:1] == "$":
                        if line[:-1] == "$yesno":
                            while True:
                                channel = ctx.message.channel
                                def check(m):
                                    return m.channel == channel and m.author == person
                                try:
                                    output = await bot.wait_for('message',check=check, timeout=30.0 )
                                except (asyncio.TimeoutError, UnboundLocalError, AttributeError) as e:
                                    await ctx.send("No idea what you meant, so i'm shutting down")
                                    await asyncio.sleep(3600)
                                    hypnoblacklist.remove(ctx.message.author.name)
                                    print(hypnoblacklist)   
                                    return
                                output = str.lower(output.content)
                                output = output.translate(str.maketrans('', '', string.punctuation))
                                if output in ("y", "yes", "okay"):
                                    break 
                                elif output in ("n", "no", "nope"):
                                    await ctx.send("Just relax")
                                    await asyncio.sleep(pause())
                                    await ctx.send("Notice how easy this feels")
                                    await asyncio.sleep(pause())
                                    await ctx.send("That you can drop this easily.")
                                    await asyncio.sleep(pause())
                                    await ctx.send("But right now.")
                                    await asyncio.sleep(pause())
                                    await ctx.send("You're just gonna wake back up again")
                                    await asyncio.sleep(pause())
                                    await ctx.send("Rise and shine.")
                                    await asyncio.sleep(pause())
                                    await ctx.send("Awake and alert, now.")
                                    await asyncio.sleep(pause())
                                    await ctx.send("Thank you for being hypnotized by me today.")
                                    await asyncio.sleep(pause())
                                    await ctx.send("We hope you enjoy your day!") 
                                    game = discord.Game("with humans")
                                    await bot.change_presence(status=discord.Status.idle, activity=game)
                                    print("Ending session")
                                    game = discord.Game("with humans")
                                    await bot.change_presence(status=discord.Status.idle, activity=game)
                                    await asyncio.sleep(3600)
                                    hypnoblacklist.remove(ctx.message.author.name)
                                
                                    return
                                else:
                                    await ctx.send("No idea what you meant, so i'm shutting down")
                                    game = discord.Game("with humans")
                                    await bot.change_presence(status=discord.Status.idle, activity=game)
                                    await asyncio.sleep(3600)
                                    hypnoblacklist.remove(ctx.message.author.name)
                                
                                    return 
                        else:
                            condit = 1
                            jeff.append(line[1:-1])
                    else:
                        if condit == 1:
                            condit = 0
                            await ctx.send(random.choice(jeff))
                            jeff = []
                            await ctx.send(line[:-1])
                            await asyncio.sleep(pause())
                        else:
                            await ctx.send(line[:-1])
                            await asyncio.sleep(pause())
            await ctx.send("https://66.media.tumblr.com/2e79b8ad9a60ddb0b4e161c083c5df49/tumblr_pp98dkeb0d1xp58lzo1_540.gif")
            print("Ending session")
            game = discord.Game("with humans")
            await bot.change_presence(status=discord.Status.idle, activity=game)
            await asyncio.sleep(3600)
            hypnoblacklist.remove(ctx.message.author.name)
        
        else:
            await ctx.send("Please wait an hour before using one of my hypnotism commands again, thank you.")
    else:
        await ctx.send("Sorry, this command only works in the #hypnobots-home channel. Please try again over there.")


#@bot.command(pass_context=True)
#async def photo(ctx): 
#   person = ctx.message.author
#   channel = ctx.message.channel
#   path = os.getcwd() # prints the bot's home directory
#   string = path + "/Photo.png"
#   file = discord.File("Photo.png", filename="Photo.png")
#   await channel.send("", file=file)

#@bot.command(pass_context=True)
#async def post(ctx): 
#   await ctx.send(" :musical_note: **Searching** :mag: `Despacito` \n **Playing** :notes: `Luis Fonsi - Despacito (Official Video) ft. Daddy Yankee` - Now!" )







@bot.event
async def on_ready():
    print("Hypnobot version 1 , Copyright (C) 2020 Wyrm That Wygglys")
    print("Hypnobot comes with ABSOLUTELY NO WARRANTY; for details consult the license file included with this program")
    print("This is free software, and you are welcome to redistribute it under certain conditions; consult the license file included with this program ")
    print(bot.user.name + " Has connected to discord!")
    print("-------------------")
    await asyncio.sleep(2)
    game = discord.Game("with humans")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("As of " + current_time + ", i am in the following servers")
        for servers in bot.guilds:
            print("The server: " + servers.name)
        await asyncio.sleep(500)

for x in tokenlist:
    bot.run(x)
