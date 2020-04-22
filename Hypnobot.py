# bot.py
import os
import discord
from discord.ext import commands
import asyncio
import json
import random 
import sys
import time

BOT_PREFIX = ("?", "!")
tokenlist = ["NTU2OTg2NjUwMDA2MjU3Njc1.D3Bu-Q.AvhrK-F0Z8NYktMUVvu-R72x5pg", ]
bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command("help")
client = discord.Client()

@bot.command(pass_context=True)
async def help(ctx):
	person = ctx.message.author
	await asyncio.sleep(2)
	await ctx.send("Hello. I am a sweet, innocent hypnobot programmed by nWo Bloof for various hypnosis servers. My commands are:\n!hello\nMakes me say hi to you,\n!yes\nMakes me agree with you,\n!no\nMakes me disagree with you,\n!dance\nMakes me dance,\n!stop\nMakes me drop into trance for five seconds,\n!repeat\nMakes me repeat whatever you say immediately afterwards,\n!hug\nGives me a hug from you,\n!pet\nThat gives me a headpat from you,\n!trance\nA command for a special learning script designed to help take people into trance.\n Please feel free to give me hugs, I really like them a lot!")
	
@bot.command(pass_context=True)
async def hello(ctx):
	person = ctx.message.author
	await asyncio.sleep(2)
	await ctx.send("Hello, " + person.mention + "!")

@bot.command(pass_context=True)
async def yes(ctx):
	person = ctx.message.author
	await asyncio.sleep(2)
	await ctx.send("Of course, " + person.mention + "!")

@bot.command(pass_context=True)
async def no(ctx):
	person = ctx.message.author
	await asyncio.sleep(2)
	await ctx.send("Of course not, " + person.mention + "!")

@bot.command(pass_context=True, aliases=["hugs"])
async def hug(ctx):
	person = ctx.message.author
	await asyncio.sleep(2)
	await ctx.send("Mmmmm! Thank you, " + person.mention + "!")

@bot.command(pass_context=True, aliases=["petpetpet"])
async def pet(ctx):
	person = ctx.message.author
	await asyncio.sleep(2)
	await ctx.send("Ehehehe! That tickles, " + person.mention + "!")

@bot.command(pass_context=True)
async def dance(ctx):
	await ctx.send("https://66.media.tumblr.com/2e79b8ad9a60ddb0b4e161c083c5df49/tumblr_pp98dkeb0d1xp58lzo1_540.gif")

@bot.command(pass_context=True)
async def stop(ctx):
	await ctx.send("https://66.media.tumblr.com/376ebf73ef1065e3125c668db59b3cf8/tumblr_pp9e1uPyEq1xp58lzo1_540.gif")
	game = discord.Game("Uuuh, sleepies")
	await bot.change_presence(status=discord.Status.idle, activity=game)
	await asyncio.sleep(1)
	await asyncio.sleep(1)
	await asyncio.sleep(1)
	await asyncio.sleep(1)
	await asyncio.sleep(1)
	await ctx.send("Uhhh, i'm back.")
	game = discord.Game("with humans")
	await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command(pass_context=True)
async def trance(ctx): 
	person = ctx.message.author
	if ctx.message.channel.id == 701913614801436872 or ctx.message.channel.id == 557225192158527490:
		output3 = "" 
		output2 = ""
		output1 = "" #The last three lines of the induction
		path = os.getcwd() # prints the bot's home directory
		access_rights = 0o755 #755, readable and writable anywhere
		print(" Doing a session. The current working directory is %s" % path)
		game = discord.Game("with " + str(person) + "'s head")
		
		await bot.change_presence(status=discord.Status.idle, activity=game)
		await ctx.send("This is a super experimental hacky script, designed to take you into trance. Are you sure you wanna continue," + person.mention + "? Say yes if you agree.")
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
				return
			output = str.lower(output.content)
			if output in ("y", "yes", "yes ","yes.", "okay",  "okay."):
				await ctx.send("Okay")
				break 
			elif output in ("n", "no", "nope"):
				await ctx.send("Understood. Shutting down")
				game = discord.Game("with humans")
				await bot.change_presence(status=discord.Status.idle, activity=game)
				print("Ending session")
				return
			else:
				await ctx.send("No idea what you meant, so i'm shutting down")
				game = discord.Game("with humans")
				await bot.change_presence(status=discord.Status.idle, activity=game)
				print("Ending session")
				return
		await ctx.send("Make sure you're nice and comfortable before we begin.")
		await asyncio.sleep(2)
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
					return
				output = str.lower(output.content)
				if output in ("y", "yes", "okay"):
					await ctx.send("Okay")
					break 
				elif output in ("n", "no", "nope"):
					await ctx.send("Understood. Shutting down")
					game = discord.Game("with humans")
					await bot.change_presence(status=discord.Status.idle, activity=game)
					print("Ending session")
					return
				else:
					await ctx.send("No idea what you meant, so i'm shutting down")
					game = discord.Game("with humans")
					await bot.change_presence(status=discord.Status.idle, activity=game)
					print("Ending session")
					return        
			try:  
				os.mkdir(newpath, access_rights)
				await ctx.send("Successfully created the directory " + newpath)
			except OSError:  
				await ctx.send("Creation of the directory " + newpath + " has failed. Please consult my programmers for more information, and have a nice day!")
				return
			dictionary = {
				"trance": 2,
				"mind": 2,
				"blank": 2,
				"sleepy": 2,
				"relaxed": 2,
				"mindless": 1,
				"obedience": 2,
				"pleasing": 2,
				"entranced": 2,
				"repeat": 6,
			}
			with open(newpath + "trances.txt", "w") as outfile:  
				json.dump(dictionary, outfile)
		else:   
			await ctx.send("We have your data on file. Loading...")

			with open(newpath + "trances.txt") as json_file:  
				dictionary = json.load(json_file)

		await ctx.send("So what we're going to do is play a little game, alright?")
		await asyncio.sleep(2)
		await ctx.send("I'm going to say a word, and you're going to say the first thing that pops into your head")
		await asyncio.sleep(2)
		await ctx.send("And as we go on, i'd like you to notice how we keep coming back to the same words")
		await asyncio.sleep(2)
		await ctx.send("Over and over, again and again.")
		await asyncio.sleep(2)
		await ctx.send("So let's take a deep breath now, and begin")
		await asyncio.sleep(2)
		await ctx.send("Your first word is...")
		await asyncio.sleep(2)
		await ctx.send("Trance")
		while True: 
			try:
				output1 = await bot.wait_for('message',check=check, timeout=30.0 )
			except (asyncio.TimeoutError, UnboundLocalError, AttributeError) as e:
				print(e)
				await ctx.send("I guess you're not here, so i'm shutting down.")
				print("Ending session")
				return
			output1 = str.lower(output1.content)
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
			await asyncio.sleep(2)
			await ctx.send(random.choice(dartboard).capitalize())
		await asyncio.sleep(2)
		await ctx.send(output)
		await asyncio.sleep(2)
		await ctx.send("It's okay if you wanna keep repeating that word")
		await asyncio.sleep(2)
		await ctx.send("Type it out over and over again")
		await asyncio.sleep(2)
		await ctx.send("Cause it's easy")
		await asyncio.sleep(2)
		await ctx.send("It's simple")
		await asyncio.sleep(2)
		await ctx.send("It comes so naturally to you")
		await asyncio.sleep(2)
		await ctx.send("That word can become your mantra")
		await asyncio.sleep(2)
		await ctx.send("It's so easy to keep repeating") 
		await asyncio.sleep(2)
		await ctx.send("And it can drop you down deep") 
		await asyncio.sleep(2)
		newvalue = dictionary[output1] + 50
		dictionary[output1] = newvalue 
		with open(newpath + "trances.txt", "w") as outfile:  
			json.dump(dictionary, outfile)
		await ctx.send("But now, let's wake back up again") 
		await asyncio.sleep(2)
		await ctx.send("In 3") 
		await asyncio.sleep(2)
		await ctx.send("2")
		await asyncio.sleep(2)
		await ctx.send("1")  
		await asyncio.sleep(2)
		await ctx.send("Rise and shine, awake and alert") 
		await asyncio.sleep(2)
		await ctx.send("Thank you for being hypnotized by me today.")
		await asyncio.sleep(2)
		await ctx.send("We hope you enjoy your day!") 
		game = discord.Game("with humans")
		await bot.change_presence(status=discord.Status.idle, activity=game)
		print("Ending session")
	else:
		await ctx.send("Sorry, this command only works in the #hypnobots-home channel. Please try again over there.")
		

@bot.command(pass_context=True)
async def repeat(ctx, arg):
	await ctx.send(arg)

@bot.event
async def on_ready():
	print(bot.user.name + " Has connected to discord!")
	await asyncio.sleep(2)
	game = discord.Game("with humans")
	await bot.change_presence(status=discord.Status.idle, activity=game)
	while True:
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		print("As of " + current_time + ", i am in the following servers")
		for servers in bot.guilds:
			print("The server: " + servers.name) 
		await asyncio.sleep(120)	
	
for x in tokenlist:
	bot.run(x)