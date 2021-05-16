import json
import sqlite3
from datetime import datetime, date

#initialize db

conn = sqlite3.connect('shoes_database.db')

#create products table
#id_no autoincrements, is a number
#id_no, product_id, message_id, style_color, webhook_token, stock_level
# conn.execute("DROP TABLE shoe_products")

conn.execute("""CREATE TABLE IF NOT EXISTS shoe_products(
              id_no INTEGER PRIMARY KEY AUTOINCREMENT, 
              product_id TEXT NOT NULL, 
              message_id TEXT, 
              style_color TEXT, 
              webhook_token TEXT, 
              stock_level TEXT,
              date_created DATETIME NOT NULL
              )
      """
)

#create parse_items table
#id_no, webhook_id, webhook_token, country_code, url

# conn.execute("DROP TABLE parse_items")
conn.execute("""CREATE TABLE IF NOT EXISTS parse_items(
              id_no INTEGER  PRIMARY KEY AUTOINCREMENT, 
              webhook_id TEXT NOT NULL , 
              webhook_token TEXT, 
              country_code TEXT,
              url TEXT 
          )"""
)

#create credentials table
# conn.execute("DROP TABLE credentials_table")
conn.execute("""CREATE TABLE IF NOT EXISTS credentials_table(
              bot_token TEXT NOT NULL PRIMARY KEY,
              channel_id TEXT
            )"""
)
#bot_token, channnel_id


def read_parse_items(filename):
    with open(filename, 'r') as file:
      dict = json.load(file)
    return dict

#product table
def createProduct(product_id, message_id, style_color, webhook_token, stock_level):
  #Adding the product to the database
  conn.execute("""INSERT INTO shoe_products(product_id, message_id, style_color, webhook_token, stock_level, date_created) 
                    VALUES(?,?,?,?,?,?)
              """, (product_id, message_id, style_color, webhook_token, stock_level, datetime.now()))
  #Saving to database
  conn.commit()
  return


def getProduct(id_no):
  #get product
  product = conn.execute("""SELECT  product_id, message_id, style_color, webhook_token, stock_level, date_created, id_no from shoe_products where ?""", str(id_no))
  #parse product 
  for row in product: 
    item = {
      "id_no": row[6],
      "product_id": row[0],
      "message_id": row[1],
      "style_color": row[2],
      "webhook_token": row[3],
      "stock_level" : row[4],
      "date_created" : row[5]
    }
  return item 

def count_products():
  #select count
  cursor = conn.cursor()
  count = cursor.execute("""SELECT COUNT(product_id) FROM shoe_products""")
  return count.fetchone()[0]

def updateProduct(id_no, stock_level):
  #update the table
  c = conn.cursor()
  c.execute("""UPDATE shoe_products set stock_level = ? where id_no = ?""",( stock_level ,id_no))
  conn.commit()
  return
  


def createParse_items(filename):
  parseItems = read_parse_items(filename)

  #loop and save
  #params of looped item : webhook_id, webhook_token, country_code, url
  for item in parseItems["objects"]:
    webhook_id = item["webhook_id"]
    webhook_token = item["webhook_token"]
    country_code = item["country_code"]
    url = item["url"]

    conn.execute("""
      INSERT INTO parse_items (webhook_id, webhook_token, country_code, url)
      VALUES(?,?,?,?)
    """, (webhook_id, webhook_token, country_code, url))
  conn.commit();
  return

def getParseItem(id_no):
  parse_items = conn.execute("""SELECT id_no, webhook_id, webhook_token, country_code, url FROM parse_items where id_no = ?""", str(id_no))
  for row in parse_items:
    item= {
      "id_no" : row[0],
      "webhook_id" : row[1],
      "webhook_token" : row[2],
      "country_code" : row[3],
      "url" : row[4]
    }
  return item

def count_parse_items():
  #select count
  cursor = conn.cursor()
  count = cursor.execute("""SELECT COUNT(*) FROM parse_items""")
  return count.fetchone()[0]


def addCredentials(bot_token, channel_id):
  #Adding credential
  cursor = conn.cursor()
  c = cursor.execute("""SELECT COUNT(*) FROM credentials_table""")
  count=  c.fetchone()[0]
  if(count == 0):
    conn.execute("""INSERT INTO credentials_table (bot_token, channel_id) VALUES(?,?)""", (bot_token, channel_id))
    conn.commit()
  return
  

def getCredentials():
  cursor = conn.execute("""SELECT channel_id, bot_token FROM credentials_table""")
  for row in cursor:
    item = {
        "channnel_id" : row[0],
        "bot_token" : row[1]
      }

  return item


def parse_items_is_empty():
  #select count from parse_items
  if count_parse_items() == 0:
    return True
  else:
    return False

def credentials_is_empty():
  #select count from credentials
  cursor = conn.cursor()
  c = cursor.execute("""SELECT COUNT(*) FROM credentials_table""")
  count=  c.fetchone()[0]
  if(count == 0):
    return True
  else:
    return False

def update_credentials(bot_token, channnel_id):
  #delete all data from credentials table
  sql = 'DELETE FROM credentials_table'
  conn.execute(sql)
  conn.commit()
  #add new credentials
  addCredentials(bot_token,channnel_id)
  
def update_parseItems(filename):
  #delete all data from parse_items table
  update_parse = 'DELETE FROM parse_items'
  conn.execute(update_parse)

  return 

  #insert new data
  createParse_items(filename)
  



#closing the database 
#conn.close()
