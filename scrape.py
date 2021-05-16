import requests #making standard html requests
from bs4 import BeautifulSoup##parsing html data
import datetime
import discordCl
import stockLevel


# print(soup.find_all(attrs={'class':'card-link d-sm-b'}))
# print(scraped_data)




def extract_thumbnail(code):
  return 'https://secure-images.nike.com/is/image/DotCom/'+code.replace('-','_')+'_A_PREM?$SNKRS_COVER_WD$&amp;align=0,1'



def get_productId_dictionary(productId, countryCode):
  url = 'https://api.nike.com/merch/skus/v2/?filter=productId('+productId+')&filter=country('+countryCode+')'


  res = requests.get(url = url)
  return res.json()



def scrape_data_from(url, country_code, webhook):
  #Requesting data from our target url
  page = requests.get(url)

  page.encoding = 'ISO-885901' #makingsure requests correctly parses the content
  soup = BeautifulSoup(page.text, 'html.parser')
  #Viewing the entire code in terminal
  # print(soup.prettify())

  scraped_data = soup.find_all(attrs={'class':'card-link d-sm-b'})
  print("fining data")
  for data in scraped_data:
    if(data.get('aria-label')):
      altname = data.get('aria-label')
      link = data.get('href')
      print(altname)
      print("https://www.nike.com"+link)
      mini_page =requests.get("https://www.nike.com"+link)
      mini_page.encoding = 'ISO-885901' #makingsure requests correctly parses the content
      mini_soup = BeautifulSoup(mini_page.text, 'html.parser')

      # get product id
      if(mini_soup.find('meta', attrs={'name':'branch:deeplink:productId'})):
        product_id = mini_soup.find('meta', attrs={'name':'branch:deeplink:productId'})['content']
      else:
        continue
      print(product_id)

      # get style_color
      style_color = mini_soup.find('meta', attrs={'name':'branch:deeplink:styleColor'})['content']
      print(style_color)

      # extract thumbnail from style color
      thumbnail = extract_thumbnail(style_color)
      print(thumbnail)


      if(mini_soup.find(attrs={'class':'ncss-col-sm-12 full'})):
        mini_data = mini_soup.find(attrs={'class':'ncss-col-sm-12 full'})
        shoe_name_1 = mini_data.find('h1').getText()
        shoe_name_2 = mini_data.find('h5').getText()
        shoe_name = shoe_name_1 + ' '+shoe_name_2
        print(shoe_name)
        # getting price
        price = mini_data.find('div', attrs={'class':'headline-5'}).getText()
        print(price)
        # getting date
        month = data.find('p', attrs={'data-qa': 'test-startDate'}).getText() 
        print(month)
        date = data.find('p', attrs={'data-qa': 'test-day'}).getText()
        print(date)

        month_name = month
        datetime_object = datetime.datetime.strptime(month_name, "%b")
        month_number = datetime_object.month
        print(month_number)
      

        productId_file = get_productId_dictionary(product_id, country_code)
        # print(stylecolor_file)
        # print(stylecolor_file)
        stockLevel_str = stockLevel.get_stocklevels(productId_file, style_color)
        
        message_data = {
            # "username" : "GhostBot",
            "embeds": [{
                
                "title": shoe_name,
                "url": "https://www.nike.com"+link,
                "fields": [
                    {
                        "name" : "Date",
                        "value": str(month_number)+"/"+date+"/2021"
                    },
                {
                        "name" : "Style Code",
                        "value": style_color
                    },
                {
                        "name" : "Price",
                        "value": price
                    },
                {
                        "name" : "Stock Level",
                        "value": stockLevel_str
                    },
                {
                    "name" : "Stock Level Indicator",
                    "value" : "<:green:838427974805094461> - HIGH <:orange:838427817204645888> - MEDIUM  <:red:838427974809944115> -LOW <:sign:838429554645270558> - OOS"
                },
                {
                    "name" : "Early Link",
                    "value" : "```https://www.nike.com"+link+"?productId="+product_id+"&size=```\n*insert your desired size behind the link*"
                }
                
                
                ],
                "thumbnail" : {
                    "url" : thumbnail
                },   
                "color": 16777215, 
                "footer": {
                    "text" : "GHOST SUPPLY TEAM",
                    "icon_url" : "https://secure-images.nike.com/is/image/DotCom/DJ6903_100_A_PREM?$SNKRS_COVER_WD$&align=0,1" 
                }
            }]
        }
        #send data to discord
        discordCl.send_message(message_data, webhook)

        #incolaborate api to listedn for message id


        #save to database, message_id, webhook_name, stockLevel

