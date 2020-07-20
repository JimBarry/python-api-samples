from arcgis.gis import GIS
from IPython.display import display
from getpass import getpass

# ---------------------

#get inputs from user
ptl = input('enter arcgis online org name: ')
unm = input('enter username: ')
pwd = getpass('enter password: ')
srt = input('enter feature layer search term: ')

# ---------------------

# connect to org
gis = GIS("https://" + ptl + ".maps.arcgis.com", username=unm, password=pwd)

# ---------------------

# search items by keyword, show basic results
my_content = gis.content.search(srt, item_type="Feature Layer")
my_content

# ---------------------

# show full results
for item in my_content:
    display(item)




