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
# Tumor-X
""")

uploaded_file = st.file_uploader("Upload Your image", accept_multiple_files=False)
if uploaded_file is not None:
    col1, col2 = st.columns([1, 2])
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption='User uploaded Image')
    fig = view_classify(image, model)
    with col2:
        st.plotly_chart(fig, use_container_width=True)
