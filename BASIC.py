from arcgis.gis import GIS
from IPython.display import display
from getpass import getpass

ptl = input('enter portal name: ')
unm = input('enter username: ')
pwd = getpass('enter password: ')

gis = GIS("https://" + ptl + ".maps.arcgis.com", username=unm, password=pwd)

my_content = gis.content.search("nyc", item_type="Feature Layer")
my_content

for item in my_content:
    display(item)
