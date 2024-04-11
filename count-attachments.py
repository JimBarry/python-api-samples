# -----

from arcgis.gis import GIS
portalId_HostedFeatureService = '904467ee2fbb45f1ac816dd5ff3768ed'
gis = GIS('home')
print(gis)

# -----

hfl_item = gis.content.get(portalId_HostedFeatureService)
hfl_layer = hfl_item.layers[0] 'just the first feature layer in the feature service
hfl_fset = hfl_layer.query()
hfl_features = hfl_fset.features
attachments = hfl_layer.attachments
print(hfl_item.url)

# -----

countFeatures = 0
countAttachments = 0
for feat in hfl_features:
    countFeatures+=1
    attribs = feat.attributes
    oid = attribs.get('OBJECTID')
    attach = attachments.get_list(oid)
    numAttachments = len(attach)
    countAttachments = countAttachments + numAttachments
    strToPrint = 'record: ' + str(countFeatures) + ', OID: ' + str(oid) + \
                 ', num attachments: ' + str(numAttachments)
    print(strToPrint)
print('------------------------------------------')    
strTally = 'Total feature records: ' + str(countFeatures) + \
           ', Total Attachments: ' + str(countAttachments)
print(strTally)

# -----
