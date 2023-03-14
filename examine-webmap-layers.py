from arcgis.gis import GIS
from arcgis.mapping import WebMap

# enter your org/username/password below
gis = GIS("https://your_org.maps.arcgis.com", "your_username", "your_password") 

# searching for all web maps that have the word "NYC" in their titles
my_content = gis.content.search("NYC", item_type="Web Map")
my_content

# list all layers in every web map
for item in my_content:
    wm = WebMap(item)
    print("Web Map: " + item.id)
    layers = wm.layers
    for layer in layers:
        if layer.get("url") != None:
            print("  " + layer["url"])
            
# RESULTS END UP LOOKING LIKE THIS:

# Web Map: 5a902c7994674f17b4a95cf0998dac3d
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/nyc_bikeracks/FeatureServer/0
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/nypd_companies/FeatureServer/0
# Web Map: 658d878f61c14f4ebafa099e72e6a016
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_Public_Schools/FeatureServer/0
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_Communities/FeatureServer/0
# Web Map: a046a7f0ac4d456e996059e18b176fbd
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC%20Bicycle%20Lanes/FeatureServer/0
# Web Map: db413742fb9c40f7a3972d49b100612c
#   https://jimbarry.github.io/csvs/FDNY_Firehouse_Listing.csv
#   https://www.arcgis.com/sharing/rest/content/items/f02996df144148f59226b634d03681be/data
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_BOROUGHS/FeatureServer/0
# Web Map: e72de035b46443a9a7a6fb89aeee3571
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/bike_racks/FeatureServer/0
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_Community_Dists/FeatureServer/0
# Web Map: 24f7f93ae091403d9c3717c7fb83a0ec
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC311_ComDist_317/FeatureServer/0
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_CommunityDistrict_317/FeatureServer/0
# Web Map: 005606adbb94438ab511b61f7b705430
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/Public_School_Locations_hfl/FeatureServer/0
# Web Map: 1d38a0e811094836a07c2f7c0ee43609
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/Bicycle_Parking_NYC/FeatureServer/0
# Web Map: aecdd5431fd446dbb176a9dc131384f4
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/FDNY_Firehouse_Listing3/FeatureServer/0
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_BOROUGHS/FeatureServer/0
# Web Map: aa37d620277847a593af4e3b1b051786
#   https://services9.arcgis.com/hsPsr2XddCBblVhb/arcgis/rest/services/NYC_BOROUGHS/FeatureServer/0

