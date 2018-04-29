
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

customers = db["customers"]
person = {

}
count_wom = 0
count_ads = 0
count_events = 0
all_customer = customers.find()
for person in all_customer:
    if person["ref"] == "wom":
        count_wom += 1
    elif person["ref"] == "ads":
        count_ads += 1
    elif person["ref"] == "events":
        count_events += 1

count_ref = {
    'ads': count_ads,
    'wom': count_wom,
    'events': count_events
}

print(count_ref)

machine_counts = count_ref.values()
machine_names = count_ref.keys()
pyplot.pie(machine_counts, labels=machine_names,autopct="%.1f%%", explode=[0,0.2,0])
pyplot.title("Percentage of each references")
pyplot.axis("equal")

pyplot.show()
