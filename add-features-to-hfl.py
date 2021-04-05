from arcgis.gis import GIS
from getpass import getpass

# get user input of agol portal name, user name, and password
ptl = input('enter arcgis online org name: ')
unm = input('enter username: ')
pwd = getpass('enter password: ') 

gis = GIS("https://" + ptl + ".maps.arcgis.com", username=unm, password=pwd)

# search for feature layers using a user input search term
srt = input('enter search term: ')
my_content = gis.content.search(srt, item_type="Feature Layer")

# display the results of the search
my_content

idx = input('which layer do you want? (if first item, just hit enter): ') or 0

# gets the selected item
my_flayer_item = my_content[int(idx)]

# gets the first layer from the selected item
my_flayer = my_flayer_item.layers[0]

# schema and values must match the layer you're editing
newtrain_dict = {"attributes": {"MYID": 5, "NAME": "foxtrot", "DESCRIP": "zeta"},
                 "geometry": {"x": -118.23, "y": 33.72, "spatialReference" : {"wkid" : 4326}}}

# assumes this hosted feature layer is editable
add_result = my_flayer.edit_features(adds = [newtrain_dict])

# if edit is successful, results will be printed below
add_result
