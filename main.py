
import scrape
import json

# scrape.scrape_data_from('https://www.nike.com/launch?s=upcoming','US')

#method to save webhook links
def getWebhooks(webhooksFile):
  #algos
  return

#check for needed data from database, if not in database, request data from input

#api token

#channel_id

#webhook links
#check if table is empty, if empty ask for json file




def get_links():
    with open('test.json', 'r') as file:
      dict = json.load(file)
    return dict




links = get_links()

for link in links['objects']:
  country_code = link['country_code']
  url = link['url']
  webhook = link['webhook']
  print('scraping '+link['country_name'])
  scrape.scrape_data_from(url, country_code, webhook)



#two threads

#thread one: scrape data from site


#thread two: check for updates



#they wont work bro.
#japan link: https://www.nike.com/jp/launch?s=upcoming