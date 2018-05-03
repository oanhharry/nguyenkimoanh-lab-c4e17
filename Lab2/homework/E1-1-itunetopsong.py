from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"

#1 open connection
conn = urlopen(url)

raw_data = conn.read()
text = raw_data.decode('utf8')

soup = BeautifulSoup(text, "html.parser")

section = soup.find("section", "section chart-grid")
# print(section.prettify)

section_list = section.find_all("li")
# print(section_list)

item_list = []
for section in section_list:
    # print(section.prettify)
    a = section.h3.a
    b = section.h4.a
    name = a.string
    author = b.string
    print(name)
    print(author)

    item = {
        "Name": name,
        "Author": author,
    }
    item_list.append(item)
# print(item_list)
pyexcel.save_as(records=item_list, dest_file_name="itunetopsong.xlsx")
