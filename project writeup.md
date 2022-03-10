### Project overview
Object Detection in an Urban Environment project is ment to use pretrained Convolutional Neural Network CNN SSD Resnet 50 640x640 model to show basical principles of using pretrained model for object detection by using [Waymo Open dataset](https://waymo.com/open/). In this project pretrained model will be used to retrain and than used for validationa and testing.
Self driving cars need information of their surroundings and they receive this information from the sensors like camera, Lidar, Radar etc. and base on this information they decide for their actions. Object detection is one of the most important concepts in Self-Driving cars because by object detection self driving car can identify oder participants on the road like other cars, cyclist, pedestrians etc.

### Set up
In order to use this project, project files should be obtained from [GitHub repository](https://github.com/atanasko/Object-Detection-in-an-Urban-Environment.git).
Project code can be executed localy only on a machine with Nvidia GPU and appropriate libraries. Python 3 is also required on a local machine. In order to execute Jupyter notebooks appropriate package is required locally installed.

### Dataset
#### Dataset analysis

During the dataset exploratory analysis we can notice that most of the images are taken in urban environment and on a sunny weather. There are some of the images on the open road. Very few of the images are in rainy, cloudy and night weather.

Here are some images from the analysis

![Alt text](results/exploratory_data_analysis/frame1.png "First test result")

*Note: Images can be seain the in the github notebook presentation. In the notebook there are filenames of the multiple test records.* 

#### Cross validation

Data set is splitted in training and validation subsets. Splitting is done following the rule 80% - 90% goes in the training dataset, and the 10% - 20% goes in validation dataset.

### Training
#### Reference experiment

During the training process learning curve rise lineary and than drop non non lineary. Loss function have different form when training performed on the same training model from beggining. Screenshots from the training and test are attached in the result directory.

#### Improve on the reference

This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
