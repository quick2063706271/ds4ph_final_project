## Introduction.py

from PIL import Image
import streamlit as st

st.write("""
# Introduction

Brain tumor is one of the most severe tumor types among all. Globally, there are about 3.7 in 100,000 males and about 2.6 in 100,000 females having primary malignant brain tumor. In 2007 in the United States, there are approximately 20,000 individuals were diagnosed with primary brain tumors. The mortality is about 2.8 in 100,000 for males and about 2.0 in 100,000 for females worldwide (Bondy et al., 2008).

We developed and trained a Magnetic Resonance Imaging (MRI) brain tumor imaged-based Convolutional Neural Network (CNN) to classify MRI brain tumor images, and then incorporate the classifier into a web application.

The dataset we utilized has already classified brain tumor types into 4 categories: glioma tumor, meningioma tumor, pituitary tumor, and no tumor.
"""
)



image = Image.open("pages/example/Glioma tumor/glioma tumor sample_image66_annotated.jpg")
st.image(image, caption='Glioma tumor sample image')

image = Image.open("pages/example/Meningioma tumor/meningioma tumor sample_image25_annotated.jpg")
st.image(image, caption='Meningioma tumor sample image')

image = Image.open("pages/example/Pituitary tumor/pituitary tumor sample_image20_annotated.jpg")
st.image(image, caption='Pituitary tumor sample image')

image = Image.open("pages/example/No tumor/no tumor sample_image83_annotated.jpg")
st.image(image, caption='No tumor sample image', width=450)