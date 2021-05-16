import config
import json
import requests
import discord

def send_message(message, webhook): 
  
  headers = {
    'content-type' : 'application/json'
  }

  r = requests.post(url=webhook, data=json.dumps(message), headers = headers)
  print(r.text)


client = discord.Client()
client.run("ODQyNjg5NzQ5ODE0NzM4OTQ1.YJ49_A.2y24hyjxrH9tNzOfOA5a1NOl_1A")

@client.event
async def on_message(message):
    print(message.content)