from arcgis.gis import GIS
from IPython.display import display
from getpass import getpass

# ---------------------

# get user inputs
ptl = input('enter arcgis online org name: ')
unm = input('enter username: ')
pwd = getpass('enter password: ')
srt = input('enter feature layer search term: ')

# ---------------------

# connect to org
gis = GIS("https://" + ptl + ".maps.arcgis.com", username=unm, password=pwd)

# ---------------------

# search for feature layers, display basic results
my_content = gis.content.search(srt, item_type="Feature Layer")
my_content

# ---------------------

# display detailed results
for item in my_content:
    display(item)

# ---------------------

# display details of selected item
idx = input('enter index of layer you want to draw, or [enter] for 0: ') or 0
selected_item = my_content[int(idx)]
display(selected_item)

# ---------------------

# load an empty map, set extent to that of the selected layer
map1 = gis.map()
map1.extent = selected_item.extent
map1

# ---------------------

# draw feature layer into the map
map1.add_layer(selected_item)
# *** keep in mind, this sometimes takes 30-60 sec or so to draw, be patient

# end



