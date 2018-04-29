# only for MAC

import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#1 prepare database
machine_counts = [18, 4, 2]
#2 prepare label
machine_names = ["PC", "MAC", "Linux"]
#3 draw pie chart
pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f%%", explode=[0, 0.2, 0])
pyplot.title("PC vs MAC vs Linux in C4E")
pyplot.axis("equal")
#4 show
pyplot.show()
