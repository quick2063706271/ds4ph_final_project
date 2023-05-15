import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms, models
import torchvision
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
from torchvision.utils import save_image

class CNN(nn.Module):
    def __init__(self):
        self.name = 'CNN'
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 7, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(7, 12, 7)
        self.fc1 = nn.Linear(46*46*12, 32)
        self.fc2 = nn.Linear(32, 4)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 46*46*12)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x