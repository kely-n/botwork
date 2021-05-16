# import json
import requests

# def get_data(filename):
#     with open(filename, 'r') as file:
#       dict = json.load(file)
#     return dict

# stylecolor_dict = get_data('stylecolor.json')
# productId_dict = get_data('productId.json')

def get_styleColor_dictionary(styleColor, merchGroup):
  url = 'https://api.nike.com/deliver/available_gtins/v2/?filter=styleColor('+styleColor+')&filter=merchGroup('+merchGroup+')'
  res = requests.get(url = url)
  return res.json()

def get_stocklevels(productId_dict,style_color):
  
  level_string = ""
  # parse productId_dict
  for pi_object in productId_dict['objects']:
  # get pi_gtin and print it
    pi_gtin = pi_object['gtin']
    stylecolor_dict = get_styleColor_dictionary(style_color , pi_object['merchGroup'])
    # print(pi_gtin)
    size = pi_object['nikeSize']
    country = 'US'    
    localized_size = country+size
    # print(localized_size)

    

    # parse stylecolor_dict
    for sc_object in stylecolor_dict['objects']: 
  # print sc_gtin if gtin is equal to pi_gtin
      sc_gtin = sc_object['gtin']
      if pi_gtin == sc_gtin:
        # print("Equals: "+sc_gtin)
        stockLevel = sc_object['level']
        # print(stockLevel)
        sub_level_string = ""
        # ":red_circle: US7
        if stockLevel == "LOW":
          sub_level_string = "<:red:838427974809944115>" +localized_size 
          # print(sub_level_string)
          # ":orange_circle: US7
        elif stockLevel == "MEDIUM":
          sub_level_string = "<:orange:838427817204645888>" +localized_size
          # print(sub_level_string)
          # ":green_circle: US7
        elif stockLevel == "HIGH":
          sub_level_string = "<:green:838427974805094461>" +localized_size
          # print(sub_level_string)
        elif stockLevel == "OOS":
          sub_level_string = "<:sign:838429554645270558>" +localized_size
          # print("no_entry_sign: "+localized_size)
          
        if(level_string==""):
          level_string = sub_level_string
        else: 
          level_string = level_string +"\n"+ sub_level_string 
    
  # print(level_string)
  return level_string
    