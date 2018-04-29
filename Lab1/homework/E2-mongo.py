from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_default_database()
posts = db["posts"]

post = {
    'title': "Yêu C4E",
    'author': "Oanh Harry",
    'content':"Lớp chúng mình rất rất vui. Hy vọng học nhanh đến hack để giao lưu với mọi người",
}

posts.insert_one(post)

# all_posts = posts.find()
# for post in all_posts:
#     print(post)
