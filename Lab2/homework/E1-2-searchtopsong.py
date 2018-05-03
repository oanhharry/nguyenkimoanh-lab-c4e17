from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode("utf8")

soup = BeautifulSoup(text,"html.parser")
section = soup.find("section", "section chart-grid")

section_list = section.find_all("li")

item_list = []
for section in section_list:
    a = section.h3.a
    b = section.h4.a
    name = a.string
    author = b.string
    item = {
        "Name": name,
        "Author": author,
    }
    item_list.append(item)


    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1
    }
    dl = YoutubeDL(options)
    dl.download([name + author])
