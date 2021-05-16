import db

product = db.createProduct("Product", 4844848, "stylecolor", "webhook token", "Style color")

def perform():

  db.updateProduct(1, "dkfjsal")

  print(db.count_products())
  print(db.getProduct(1))

  # db.createParse_items('test.json')
  print(db.count_parse_items())

  print(db.getParseItem("1"))

  db.addCredentials("ODQyNjg5NzQ5ODE0NzM4OTQ1.YJ49_A.dqzOjEE8ZGJSf0Rb4E9H7PCP28s", "841158809384910851")
  print(db.getCredentials())

  db.update_credentials("ODQyNjg5NzQ5ODE0NzM4OTQ1.YJ49_A.dqzOjEE8ZGJSf0Rb4E9H7PCP28s", "841158809384910851")
  db.update_parseItems('test.json')
perform()
