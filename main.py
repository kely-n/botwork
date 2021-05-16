
import scrape
import json
import db
import threading

# scrape.scrape_data_from('https://www.nike.com/launch?s=upcoming','US')

#method to save webhook links
def getWebhooks(webhooksFile):
  #algos
  return

#check for needed data from database, if not in database, request data from input
if(db.credentials_is_empty()):
  #api token
  api_token = input("enter your bots api token: \n")
  #channel_id
  channel_id = input("enter your channel id: \n")
  db.addCredentials(api_token, channel_id)
  print("credentials added successfully")

#webhook links
#check if table is empty, if empty ask for json file
if(db.parse_items_is_empty()):
  print("ensure your webhooks links are well configured and in the correct format")

def check_for_updates():

  print("in check for updates")


def scrape_data():
  count = 1
  while(count<=db.count_parse_items()):
    scrape_item = db.getParseItem(count)
    scrape.scrape_data_from(scrape_item)
    if(count == db.count_parse_items()):
      count = 1
    count = count+1
    

#two threads
if __name__ == "__main__":
  #thread one: scrape data from site
  thread1 = threading.Thread(target=scrape_data())
  #thread two: check for updates
  thread2 = threading.Thread(target=check_for_updates())

  # start both threads
  thread1.start() 
  thread2.start()

#they wont work bro.
#japan link: https://www.nike.com/jp/launch?s=upcoming