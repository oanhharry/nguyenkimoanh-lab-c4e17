from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

text = raw_data.decode('utf8')

# print(text)
# VNM_file = open("VNM.html","w")
# VNM_file.write(text)
# VNM_file.close()

conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode("utf8")

soup = BeautifulSoup(text, "html.parser")
body = soup.find("div", id = "divNhom4")

table = body.find("table", id = "tableContent")
print(body)
# tbody = table.find("tbody")
# tr_list = tbody.find_all("tr")

# item_tr = []
#
# for tr in tr_list:
#     a = tr.td
#     print(a)
