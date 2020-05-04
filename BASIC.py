from arcgis.gis import GIS
from IPython.display import display

ptl = input('enter portal: ')
unm = input('enter username: ')
pwd = input('enter password: ')

gis = GIS("https://" + ptl + ".maps.arcgis.com", username=unm, password=pwd)

my_content = gis.content.search("jimbarry", item_type="Feature Layer")
my_content

for item in my_content:
    display(item)

