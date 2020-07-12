#this is a script for building a deep learning model from a folder of labeled images
#
#see developers.arcgis.com for how to install arcgis.learn
from arcgis.learn import RetinaNet, prepare_data

#folder in which you have the images and labels subfolders, relative to the current path
data_path = "images_toprocess"

#last two params can be tweaked
data = prepare_data(data_path, dataset_type='PASCAL_VOC_rectangles', batch_size=4, chip_size=500)

#displays a sample of the images you labeled with labelImg
data.show_batch()

#create a retinanet from the prepared data
#this will take a little bit to run
rn = RetinaNet(data)

#displays a chart of the learning rate
rn.lr_find()

#number of epochs, and learning rate, can be tweaked
#this will take a good while to run
rn.fit(20, lr=0.0001)

#a ground truth sample of the model, using the input images
rn.show_results()

#omg, omg, omg... always. save. the. model. ****
rn.save('name_of_saved_model')

