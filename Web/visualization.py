#Setup
import torch
import torch.nn as nn
import torchvision
import pandas as pd
import plotly.express as px
import numpy as np


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

idx_to_class = {0: 'glioma_tumor', 1: 'meningioma_tumor', 2: 'no_tumor', 3: 'pituitary_tumor'}

def view_classify(image, model):
    class_name = list(idx_to_class.values())
    classes = np.array(class_name)
    original_image = image
    image = original_image.resize((200, 200))
    image = torchvision.transforms.functional.to_tensor(image)
    image = image[None, :, :, :]
    output = model(image.to(device))
    m = nn.Softmax(dim=1)
    ps = m(output)
    ps = ps.cpu().data.numpy().squeeze()
    df3 = pd.DataFrame({'classes': classes,
                        'probability': ps})

    fig = px.bar(df3, x='probability', y='classes', orientation='h', text_auto=True)
    return fig

