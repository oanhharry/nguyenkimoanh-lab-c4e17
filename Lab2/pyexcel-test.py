import pyexcel
data = [
    {
    "Name": "Huyen",
    "Age": 23,
    },
    {
    "Name": "Oanh",
    "Age": 25,
    },
    {
    "Name": "Quang",
    "Age": 29,
    }
]
pyexcel.save_as(records=data, dest_file_name="test.xlsx")
