#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Append CSV records to a hosted feature layer
##
## Given an existing hosted feature layer ("target") of points on 
## ArcGIS Online and a CSV file ("source") with the same schema with 
## new records to add, append the "source" records onto the end of the 
## existing "target" layer
##
## For more info:
## https://developers.arcgis.com/python/guide/appending-features/
##
## Also this video:
## https://www.youtube.com/watch?v=B-6AoeYQnmk (zoom ahead to 21:48)
##


# In[ ]:


import os
from arcgis.gis import GIS


# In[ ]:


portal_name = 'xxxxx'
user_name =   'xxxxx'
pwd =         'xxxxx'

gis = GIS('https://' + portal_name + '.maps.arcgis.com', user_name, pwd)


# In[ ]:


# string: path of folder in which CSVs and PNG thumbnail sit

source_csv_folder_path = os.getcwd() 
print(source_csv_folder_path)


# In[ ]:


# string: folder path + CSV file name

source_csv_file_path = os.path.join(source_csv_folder_path, "add3.csv")


# In[ ]:


# we need to upload the CSV file, creating a CSV item
# this item needs some properties like title, description,
# and at least one tag

source_csv_properties={'title':       'my new add3 CSV item',
                       'description': 'lorem ipsum',
                       'tags':        'lorem ipsum'
                      }
thumbnail_path = os.path.join(source_csv_file_path, 'testcsv.png') # optional
new_csv_item = gis.content.add(item_properties=source_csv_properties, 
                               data=source_csv_file_path, 
                               thumbnail=thumbnail_path)


# In[ ]:


# get the portal ID of the new CSV item

new_csv_item_id = new_csv_item.id
print(new_csv_item_id) # you can remove this


# In[ ]:


# Analyze the csv file to get the source_info data. 
# We need this as one of the arguments for the .append() call later in the script.
# 
# What's going on here, is that, when using a CSV as the source
# for the append, the CSV needs to be analyzed so that ArcGIS
# can try to figure out where the location information is stored.
# As long as you have columns in your CSV for Lat/Long, you should
# be fine.  X/Y is a little trickier if a projected coordinate system
# is involved. Without actual coordinate information, ArcGIS will accept
# an "Address" column, but just keep in mind that with that kind of 
# column, ArcGIS will geocode those addresses as the CSV is being 
# imported, which *does* cost credits (about $4 per 1,000), so you 
# definitely want to keep that in mind before using Address geocoding
# during publishing or appending.

analyzeItem = gis.content.analyze(file_path=source_csv_file_path, file_type='csv')
sourceInfo = analyzeItem['publishParameters'] 


# In[ ]:


# Here is where you configure which "source" columns match the "target" columns.
# You can skip this step if you are SURE the column names in the source and target
# match exactly. If any of the column names are different, then you can connect
# them this way. 
# "source" is the source CSV table's column name, "name" is the target layer's column name

fieldMappings=[{'source':'ID','name':'ID'},{'source':'GREEK','name':'ID'},
               {'source':'PHON','name':'PHON'},{'source':'LONG','name':'LONG'},
               {'source':'LAT','name':'LAT'},{'source':'VAL','name':'VAL'},
               {'source':'NOTES','name':'NOTES'}]


# In[ ]:


# search for the target layer by name

find_layers = gis.content.search('test9', item_type="Feature Layer")
find_layers # you can remove this


# In[ ]:


# if the target layer is the first in the list returned above, 
# then leave the find_layers[0] below, else change the find_layers[] index arg,
# but leave the layers[0]

target_layer = find_layers[0].layers[0]


# In[ ]:


# these are a set of parameters you can use if you're straight up appending
# new records from the source table to the bottom of the existing target layer

target_layer.append(item_id=new_csv_item_id,
                    upload_format='csv',
                    field_mappings=fieldMappings,
                    source_info=sourceInfo,
                    upsert=False,
                    skip_updates=False,
                    use_globalids=False,
                    update_geometry=True,
                    rollback=False,
                    skip_inserts=True,
                    upsert_matching_field='ID'
                    )


# In[ ]:




