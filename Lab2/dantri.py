
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"

#1 open connection
conn = urlopen(url)

#1.2 read data
raw_data = conn.read()

#1.3 decode
text = raw_data.decode('utf8')

# print(text)

# dan_tri_file = open("dantri.html","w")
# dan_tri_file.write(text)
# dan_tri_file.close()

#2 find ROI
soup = BeautifulSoup(text, "html.parser")

# print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())
li_list = ul.find_all("li")

item_list = []
for li in li_list:
    # print(li.prettify())
    a = li.h4.a
    title = a.string #string or content
    link = url + a['href']
    # print(title)
    # print(link)
    item = {
        "Title": title,
        "Link": link,
    }
    item_list.append(item)
pyexcel.save_as(records=item_list,dest_file_name="dantri.xlsx")
