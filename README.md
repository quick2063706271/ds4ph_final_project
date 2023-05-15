# PH.140.629 Final Project: MRI Brain Tumor Classifier Web App 
## Authors
Lanzhuo Wu (Team Leader),
Zhe Chen,
Yuqian Wang,
Jiaqi Yang,
Kuai Yu,

## Description
Brain tumor is one of the most severe tumor types among all. There are more than 200,000 cases per year in the United States. The five-year survival rate for brain tumors in general is only 2 out of 10 individuals.

We developed and trained a Magnetic Resonance Imaging (MRI) brain tumor imaged-based Convolutional Neural Network (CNN) to classify MRI brain tumor images, and then incorporate the classifier into a web application.

A proper MRI image classification could reduce a lot of work to the medical system as well as improve the efficiency of workflow, decreasing diagnosis cost and more importantly buy more time for the patients for early treatment.

The dataset we utilized has already classified brain tumor types into 4 categories: glioma tumor, meningioma tumor, pituitary tumor, and no tumor.

However, it is tedious and challenging to classify brain tumor type based on MRI images by human huamn.
The testing MRI files include 100 glioma tumor images, 115 meningioma tumor images, 105 no tumor images, and 74 pituitary tumor images.

The training MRI files include 826 glioma tumor images, 822 meningioma tumor images, 395 no tumor images, and 827 pituitary tumor images.

This dataset includes both front views, side views, top views, and back views.
 
We have also tried TransferLearning (TL) with AlexNet for better image classifications. Yet, there is no difference in testing accuracy. Hence, only CNN model, training data, and testing data is shown bellow.

## Run the streamlit app
```
streamlit run web.py
```

## Data Set of Choice
https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri [1]

## Model Result
Training Accuracy: 
0.9825783972125436

Validation Accuracy: 
0.8571428571428571

Testing Accuracy: 
0.7055837563451777

Our final model is two convolutional layers each followed with max pool layer, and two fully connected layers for classifications. 
```
CNN(
  (conv1): Conv2d(3, 7, kernel_size=(5, 5), stride=(1, 1))
  (pool): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  (conv2): Conv2d(7, 12, kernel_size=(7, 7), stride=(1, 1))
  (fc1): Linear(in_features=25392, out_features=32, bias=True)
  (fc2): Linear(in_features=32, out_features=4, bias=True)
)
```


## Citation
[1] Sartaj Bhuvaji, Ankita Kadam, Prajakta Bhumkar, Sameer Dedge, &amp; Swati Kanchan. (2020). <i>Brain Tumor Classification (MRI)</i> [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/1183165
