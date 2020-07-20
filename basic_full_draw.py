from arcgis.gis import GIS
from IPython.display import display
from getpass import getpass

# split cell here
ptl = input('enter arcgis online org name: ')
unm = input('enter username: ')
pwd = getpass('enter password: ')
srt = input('enter feature layer search term: ')

# split cell here
gis = GIS("https://" + ptl + ".maps.arcgis.com", username=unm, password=pwd)

# split cell here
my_content = gis.content.search(srt, item_type="Feature Layer")
my_content

# split cell here
for item in my_content:
    display(item)

# split cell here
idx = input('enter index of layer you want to draw, or [enter] for 0: ') or 0
selected_item = my_content[idx]
display(selected_item)

# split cell here
map1 = gis.map()
map1.extent = selected_item.extent
map1

# split cell here
map1.add_layer(selected_item)
# keep in mind, sometimes takes 30-60 sec or so to draw, be patient

# end



