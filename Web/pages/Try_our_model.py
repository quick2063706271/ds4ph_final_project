import streamlit as st
from PIL import Image
import torch
from visualization import view_classify
from model import CNN

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
order_dict = torch.load("./model_07.pt", map_location=device)
model = CNN()
model.load_state_dict(order_dict)
model.to(device)


st.write("""
# MRI Brain Tumor Classifier
""")

st.write("""
Our application take in a image of brain tumor Magnetic Resonance Imaging (MRI) and classify it with our trained CNN model. We support image of front views, side views, top views, and back views.
""")
st.write("""
### Categories
There are four possible result: 
- Pituitary Tumor
- No Tumor
- Meningioma Tumor
- Glioma Tumor
""")

st.write("""
### Model Result
- Training Accuracy: 0.9825783972125436

- Validation Accuracy: 0.8571428571428571

- Testing Accuracy: 0.7055837563451777
""")

st.header("Upload Your image")
uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False)
if uploaded_file is not None:
    st.header("Result")
    col1, col2 = st.columns([1, 2])
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption='User uploaded Image')
    fig = view_classify(image, model)
    with col2:
        st.plotly_chart(fig, use_container_width=True)
    st.write("""
    Base on the bar graph, we choose the highest probablility option as our classification.
    """)