# PH.140.629 Final Project: MRI Brain Tumor Classifier Web App 
## Authors
Lanzhuo Wu,
Zhe Chen,
Yuqian Wang,
Jiaqi Yang,
Kuai Yu

## Description
Brain tumor is one of the most severe tumor types among all. Globally, there are about 3.7 in 100,000 males and about 2.6 in 100,000 females having primary malignant brain tumor. In 2007 in the United States, there are approximately 20,000 individuals were diagnosed with primary brain tumors. The mortality is about 2.8 in 100,000 for males and about 2.0 in 100,000 for females worldwide (Bondy et al., 2008).

We developed and trained a Magnetic Resonance Imaging (MRI) brain tumor imaged-based Convolutional Neural Network (CNN) to classify MRI brain tumor images, and then incorporate the classifier into a web application.

As a neuroimaging, MRI plays an evolving role not only in the diagnosis of brain tumors, but also in treatment planning and post-treatment evaluation. It is one of the most frequently used detection techniques in diagnosis and one of the best (Villanueva-Meyer et al., 2017).

There are papers in recent years showing that deep learning achieves relatively high accuracy in the classification of brain tumors at a low time cost (Chmiel et al., 2023).

Bhuvaji’s group has also shown that machine learning (ML) and artificial intelligence (AI) has a consistent higher accuracy than manual classification. 

Proper classification of MRI images can reduce a significant amount of work in the healthcare system and improve workflow efficiency, reduce diagnostic costs and, more importantly, buy more time for early treatment.

The dataset we utilized has already classified brain tumor types into 4 categories: glioma tumor, meningioma tumor, pituitary tumor, and no tumor.

However, it is tedious and challenging to classify brain tumor type based on MRI images by human eyes.
The testing MRI files include 100 glioma tumor images, 115 meningioma tumor images, 74 pituitary tumor images, and 105 no tumor images.

The training MRI files include 826 glioma tumor images, 822 meningioma tumor images, 827 pituitary tumor images, and 395 no tumor images.

This dataset includes front views, side views, top views, and back views.
 
We have also tried TransferLearning (TL) with VGG16 for better image classifications (Simonyan et al. 2014). Yet, there is no difference in testing accuracy. Hence, only CNN model, training data, and testing data are shown bellow.

## Run the streamlit app
First, neviagte to Web folder
Then, run the following command
```
streamlit run Home.py
```

## Data Set of Choice
https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri (Sartaj et al., 2020)

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
[1] Bondy, M. L., Scheurer, M. E., Malmer, B., Barnholtz-Sloan, J. S., Davis, F. G., Il'yasova, D., Kruchko, C., McCarthy, B. J., Rajaraman, P., Schwartzbaum, J. A., Sadetzki, S., Schlehofer, B., Tihan, T., Wiemels, J. L., Wrensch, M., Buffler, P. A., & Brain Tumor Epidemiology Consortium (2008). Brain tumor epidemiology: consensus from the Brain Tumor Epidemiology Consortium. <i>Cancer, 113</i>(7 Suppl), 1953–1968. https://doi.org/10.1002/cncr.23741

[2]Chmiel, W., Kwiecień, J., & Motyka, K. (2023). Saliency Map and Deep Learning in Binary Classification of Brain Tumours. <i>Sensors, 23</i>(9), 4543. https://doi.org/10.3390/s23094543

[3]Sartaj Bhuvaji, Ankita Kadam, Prajakta Bhumkar, Sameer Dedge, &amp; Swati Kanchan. (2020). <i>Brain Tumor Classification (MRI)</i> [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/1183165

[4]Villanueva-Meyer, J. E., Mabray, M. C., & Cha, S. (2017). Current Clinical Brain Tumor Imaging. <i>Neurosurgery, 81</i>(3), 397–415. https://doi.org/10.1093/neuros/nyx103 

[5] Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556.
