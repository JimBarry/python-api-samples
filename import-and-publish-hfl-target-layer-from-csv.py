#!/usr/bin/env python
# coding: utf-8

# In[1]:


## IMPORT A CSV FILE TO CREATE A NEW CSV ITEM IN ARCGIS ONLINE
## THEN PUBLISH THAT CSV ITEM AS A NEW HOSTED FEATURE LAYER
##
## CSV sample data at the bottom

import os
from arcgis.gis import GIS
from IPython.display import display


# In[2]:


# connect to your ArcGIS Online account

portal_name = 'xxxxx'
user_name =   'xxxxx'
pwd =         'xxxxx'

gis = GIS('https://' + portal_name + '.maps.arcgis.com', user_name, pwd)


# In[3]:


# assuming for now that the files to import are in the CWD
data_path = os.getcwd() 
print(data_path)


# In[4]:


csv_path = os.path.join(data_path, "test9.csv")


# In[5]:


csv_properties={'title':'test9',
                'description':'lorem ipsum',
                'tags': 'lorem ipsum'}


# In[6]:


# optional: but helps if new items have thumbnail images (600x400px)

thumbnail_path = os.path.join(data_path, 'testcsv.png')


# In[7]:


# create the new CSV item

new_csv_item = gis.content.add(item_properties=csv_properties, 
                               data=csv_path, 
                               thumbnail=thumbnail_path)


# In[8]:


new_csv_item  # just a check, you can remove this


# In[9]:


# publish the new CSV item as a new hosted feature layer

new_feature_layer_item = new_csv_item.publish()


# In[10]:


new_feature_layer_item # just a check, you can remove this


# In[11]:


# if you want, you can load up a map component
# to draw the new hosted feature layer info

map1 = gis.map()
map1.extent = new_feature_layer_item.extent
map1


# In[12]:


# don't fret if your layer doesn't appear right away
# often takes 10 seconds or so to show up

map1.add_layer(new_feature_layer_item)


# In[ ]:


# test9.csv
# ID,GREEK,PHON,LONG,LAT,VAL,NOTES
# 0,ALPHA,ALPHA,-74.1,40.4,0,First Letter
# 1,BETA,BRAVO,-74.1,40.5,1,Second Letter
# 2,GAMMA,CHARLIE,-74.1,40.6,2,Third Letter
# 3,DELTA,DELTA,-74.2,40.4,3,Fourth Letter
# 4,EPSILON,ECHO,-74.2,40.5,4,Fifth Letter
# 5,ZETA,FOXTROT,-74.2,40.6,5,Sixth Letter
# 6,ETA,GOLF,-74.3,40.4,6,Seventh Letter
# 7,THETA,HOTEL,-74.3,40.5,7,Eighth Letter
# 8,IOTA,INDIA,-74.3,40.6,8,Ninth Letter
