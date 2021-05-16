import stockLevel
import db

print("hello")

count = 1

while count <= db.count_products():
  #check for updates
  #get the shoe product
  shoe = db.getProduct(count)
  

  if(count==db.count_products()):
    count = 0
  else:
    count = count + 1