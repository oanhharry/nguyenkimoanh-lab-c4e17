#pip install pymongo

#1: connect to database server

from pymongo import MongoClient
uri = "mongodb://admin:admin@ds255329.mlab.com:55329/oanhharry"
client = MongoClient(uri)

#2. get default database
db = client.get_default_database()

#3 self. get blog collection
blog = db["blog"]

#4. write a new blog
post = {
    'title': "Hôm nay trời đẹp",
    'content': "Tôi ở nhà code",
}
# blog.insert_one(post)

# blog.read()
all_posts = blog.find()

for post in all_posts:
    print(post)
