Here is the code that you can paste into a Jupyter Notebook

#FIRST CELL

 # leave these three lines here
 # nothing to edit
from arcgis.gis import GIS
from datetime import date
gis = GIS("home")


# SECOND CELL

 # replace the portalId of my feature service with yours
inspections_item = gis.content.get('d52f49495f5645f6a031aa8dbc8263f5')

 # '0' assumes the feature layer we're working with is either the only layer in the
 # feature service or the first layer in the feature service.  If the layer you're
 # working with has a different layer index, change '0' to that index.
inspections_layer = inspections_item.layers[0]

 # these three lines you can leave as-is
inspections_fset = inspections_layer.query()
num_features = len(inspections_fset)
print(num_features)


#THIRD CELL

 # we're going to loop through the records of the feature service layer one at a time
for i in range(num_features):
    
     # the rest of the code in this 'for' loop must be indented 4 spaces for it to work
     # Python uses indentations to separate code blocks.
    
     # get the feature
    feature = inspections_fset.features[i]
    
     # read the value out of the 'date_inspected' fields. If you're field is called 
     # something different, change it here
    last_inspection_datetime = int(feature.attributes['date_inspected']) / 1000
     # ( we're dividing by 1000 because the date value is in unix epoch milliseconds.
     #   and we're converting it to unix epoch seconds)
    
     # we're converting the unix epoch time of the last inspection into 
     # a python date object
    last_inspection_date = date.fromtimestamp(last_inspection_datetime)
    
     # we're getting today's date as a python date object
    today = date.today()
    
     # we're subtracting today's date with the date of the last inspection
     # to return a Python "timedelta" object, then reading the actual number 
     # of day from the timedelta object's 'days' property
    days_since_last_inspection = (today - last_inspection_date).days
    
     # then we take the number of days that have elapsed between today and
     # the last time the feature was inspected, and write that into the 
     # 'days_since_inspected' field.  If your field is called something 
     # different, change it here
    feature.attributes['days_since_inspected'] = days_since_last_inspection
    
     # then we call the layer's 'edit_features' method, passing the edited
     # feature as an array into the updates parameter
    update_result = inspections_layer.edit_features(updates=[feature])
    
 # if you're running this in a notebook, it's just handy to print out to the
 # next line that the loop, and this entire script, is 'done'
print('done')    

END OF SCRIPT
