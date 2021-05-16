import json
import sqlite3
#initialize db

conn = sqlite3.connect('shoes_database.db')
c = conn.cursor()
#create products table
c.execute("""CREATE TABlE IF NOT EXISTS products(id_no INTEGER AUTO INCREMENT, product_id TEXT NOT NULL PRIMARY KEY, message_id INTEGER, style_color TEXT, webhook_token TEXT, stock_level BLOB)""")
#id_no autoincrements, is a number
#id_no, product_id, message_id, style_color, webhook_token, stock_level


#create parse_items table
#id_no, webhook_id, webhook_token, country_code, url
c.execute("""CREATE TABLE IF NOT EXISTS parse_items(id_no INTEGER AUTO INCREMENT, webhook_id TEXT NOT NULL PRIMARY KEY, webhook_token TEXT, stock_level BLOB )""")

#create credentials table
#bot_token, channnel_id

def read_parse_items(filename):
    with open(filename, 'r') as file:
      dict = json.load(file)
    return dict

#product table
def createProduct(product_id, message_id, style_color, webhook_token, stock_level):
  #Adding the product to the database
  c.execute("""INSERT INTO products VALUES(?,?,?,?,?)""", (product_id, message_id, style_color, webhook_token, stock_level))
  #Saving to database
  product = conn.commit()
  return product


def getProduct(id_no):
  #get product
  id_no = c.execute("""SELECT id_no from products""")
  return id_no 

def count_products():
  #select count
  count = c.execute("""SELECT COUNT(*) FROM products""")
  return count

def updateProduct(id_no, stock_level):
  #update the table

  return

def createParse_items(filename):
  parseItems = read_parse_items(filename)
  #loop and save
  return

def getParseItem(id_no):
  return

def count_parse_items():
  #select count
  return

def addCredentials(bot_token, channnel_id):
  return

def getCredentials():
  return

def parse_items_is_empty():
  #select count from parse_items
  #if 0
  return True
  #if not 0
  return False

def credentials_is_empty():
  #select count from credentials
  #if 0
  return True
  #if not 0
  return False

def update_credentials(bot_token, channnel_id):
  #delete all data from credentials table

  #insert new data
  return

def update_parse_items(filename):
  #delete all data from parse_items table

  #insert new data
  parseItems = read_parse_items(filename)

  return
