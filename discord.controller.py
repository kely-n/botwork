import db
import requests
import json

print("hello")

# credentails = db.getCredentials()

# channel_id = credentails["channel_id"]
# bot_token = credentails["bot_token"]

bot_token = "ODQyNjg5NzQ5ODE0NzM4OTQ1.YJ49_A.dqzOjEE8ZGJSf0Rb4E9H7PCP28s"
#send webhook message
#parameters: message, webhook_id, webhook_token
def sendMessage(message, webhook_id, webhook_token):
  URL = "https://discord.com/api/webhooks/{}/{}".format(webhook_id, webhook_token)
  headers = {
    'content-type' : 'application/json'
  }
  r = requests.post(url=URL, data=json.dumps(message), headers = headers)
  print(r.text)
  return

# get previous message
def getCurrentMessageId(channel_id):
  URL = "https://discordapp.com/api/channels/{}/messages?limit=1".format(channel_id)
  headers = {
    'content-type' : 'application/json',
    'Authorization' : 'Bot {}'.format(bot_token)
  }

  r = requests.get(url=URL, headers=headers)
  #search for message by current webhook
  dict = r.json()
  for item in dict:
      return item["id"]
  return

#get message id after the current message id
def getMessageId(channel_id, previous_messageId, webhook_id):
  URL = "https://discordapp.com/api/channels/{}/messages?after={}".format(channel_id, previous_messageId)
  headers = {
    'content-type' : 'application/json',
    'Authorization' : 'Bot {}'.format(bot_token)
  }

  r = requests.get(url=URL, headers=headers)
  #search for message by current webhook
  dict = r.json()
  for item in dict:
    if(item["author"]["id"] == str(webhook_id)):
      return item["id"]
  #if no message will be found, check for all messages by the 
  return

def updateMessage(webhook_id,webhook_token, message_id, message):
  URL = "https://discord.com/api/webhooks/{}/{}/messages/{}".format(webhook_id, webhook_token, message_id)
  headers = {
    'content-type' : 'application/json',
    'Authorization' : 'Bot {}'.format(bot_token)
  }
  requests.patch(url=URL, data=json.dumps(message), headers = headers)
  return

def getStockLevel(channel_id, message_id):
  URL = "https://discordapp.com/api/channels/{}/messages/{}".format(channel_id, message_id)
  headers = {
    'content-type' : 'application/json',
    'Authorization' : 'Bot {}'.format(bot_token)
  }

  r = requests.get(url=URL, headers=headers)
  #search for message by current webhook
  message = r.json()
  print(message["embeds"][0]["fields"][3]["value"])
  #if no message will be found, check for all messages by the 
  return

getStockLevel(841158809384910851, 842001174702063677)

message = {
  "embeds": [
            {
                "type": "rich",
                "url": "https://www.nike.com/mx/launch/t/coleccion-de-ropa-jordan-travis-scott-verano21",
                "title": "Colección de ropa Jordan x Travis Scott",
                "color": 16777215,
                "fields": [
                    {
                        "name": "Date",
                        "value": "5/13/2021"
                    },
                    {
                        "name": "Style Code",
                        "value": "CW3169-201"
                    },
                    {
                        "name": "Price",
                        "value": "$1,999"
                    },
                    {
                        "name": "Stock Level",
                        "value": "<:green:838427974805094461>USXS\n<:sign:838429554645270558>USS\n<:green:838427974805094461>USM\n<:sign:838429554645270558>USL\n<:green:838427974805094461>USXL\n<:green:838427974805094461>US2XL\n<:sign:838429554645270558>USS\n<:green:838427974805094461>USM\n<:sign:838429554645270558>USL\n<:green:838427974805094461>USL"
                    },
                    {
                        "name": "Stock Level Indicator",
                        "value": "<:green:838427974805094461> - HIGH <:orange:838427817204645888> - MEDIUM  <:red:838427974809944115> -LOW <:sign:838429554645270558> - OOS"
                    },
                    {
                        "name": "Early Link",
                        "value": "```https://www.nike.com/mx/launch/t/coleccion-de-ropa-jordan-travis-scott-verano21?productId=85919c61-770c-5a1e-af27-b2b5ded96bd7&size=```\n*insert your desired size behind the link*"
                    }
                ],
                "thumbnail": {
                    "url": "https://secure-images.nike.com/is/image/DotCom/CW3169_201_A_PREM?$SNKRS_COVER_WD$&amp;align=0,1",
                    "proxy_url": "https://images-ext-1.discordapp.net/external/HHcHc5cLy89fb2KfmX9FbwyqcfenaqItmJv4iNC7oKI/%3F%24SNKRS_COVER_WD%24%26amp%3Balign%3D0%2C1/https/secure-images.nike.com/is/image/DotCom/CW3169_201_A_PREM",
                    "width": 821,
                    "height": 924
                },
                "footer": {
                    "text": "GHOST SUPPLY TEAM",
                    "icon_url": "https://secure-images.nike.com/is/image/DotCom/DJ6903_100_A_PREM?$SNKRS_COVER_WD$&align=0,1",
                    "proxy_icon_url": "https://images-ext-2.discordapp.net/external/gEHL-hUVOs6100LGCOOEF9j3vEd5NZ6KdJksKOWdJik/%3F%24SNKRS_COVER_WD%24%26align%3D0%2C1/https/secure-images.nike.com/is/image/DotCom/DJ6903_100_A_PREM"
                }
            }
    ]
}

updateMessage("841992654270627880","4D7xmsaYP6laPTf4zLGx3ggJryq5MonRpTOcOgEroeg3N7URQsQ-sp3-LPQMwm9M9uSa","842001187423125534",message)
print(getCurrentMessageId(841158809384910851))
print("returned: "+ getMessageId(841158809384910851 ,842001159081820182, 841992654270627880))