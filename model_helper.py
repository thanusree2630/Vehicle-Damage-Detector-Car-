from PIL import Image
import torch
from torch import nn
from torchvision import models, transforms

# Class labels
class_names = ['Front Breakage', 'Front Crushed', 'Front Normal',
               'Rear Breakage', 'Rear Crushed', 'Rear Normal']

trained_model = None  # To store loaded model globally


# Custom model using pre-trained ResNet50
class CarClassifierResNet(nn.Module):
    def __init__(self, num_classes=6, dropout_rate=0.2):
        super().__init__()
        self.model = models.resnet50(weights='DEFAULT')

        # Freeze all layers
        for param in self.model.parameters():
            param.requires_grad = False

        # Unfreeze the last block and FC layer
        for param in self.model.layer4.parameters():
            param.requires_grad = True

        # Replace final fully connected layer
        self.model.fc = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(self.model.fc.in_features, num_classes)
        )

    def forward(self, x):
        return self.model(x)


# Prediction function
def predict(image_path):
    # Load and convert image to RGB (in case of PNGs with alpha)
    image = Image.open(image_path).convert("RGB")

    # Transform: resize, tensorize, normalize
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],   # ImageNet mean
            std=[0.229, 0.224, 0.225]     # ImageNet std
        )
    ])

    # Preprocess image
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    global trained_model
    if trained_model is None:
        trained_model = CarClassifierResNet()
        trained_model.load_state_dict(torch.load("model/saved_model.pth", map_location=torch.device('cpu')))
        trained_model.eval()

    # Predict
    with torch.no_grad():
        output = trained_model(image_tensor)
        _, predicted_class = torch.max(output, 1)
        return class_names[predicted_class.item()]
