import discord;
from discord.ext import commands, tasks;
import requests;
import random;
import json;
import os #environment variable


TOKEN = os.environ['token']#replace with user bot token

intents = discord.Intents().all();
client = commands.Bot(command_prefix = '!', intents = intents);


@tasks.loop(seconds=20)
async def change_status():
    return;


@client.event
async def on_ready():
#When the bot is running, display to the console
    change_status.start();
    print('Bot ready');


@client.command(name = "color", 
                help= "Generate a random color and return color name and reference link")
async def color(ctx):
    r = random.randint(0, 255);
    g = random.randint(0, 255);
    b = random.randint(0, 255);

    url = 'https://www.thecolorapi.com/id?rgb=' + str(r) + ',' + str(g) + ','+ str(b);

    response = requests.get(url);
    data = response.json();  
  
    embed = discord.Embed(title = data['name']['value'],
                          description = "", 
                          color = discord.Color.from_rgb(r, g, b),
                          url = data['image']['named']
    );
  
    await ctx.send(embed=embed);


client.run(TOKEN);