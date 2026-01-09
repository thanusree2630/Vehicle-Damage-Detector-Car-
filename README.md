# Car Damage Detector

A deep learning-powered application that analyzes vehicle images to identify and classify damage automatically. Built with Streamlit and ResNet50, this tool enables quick damage assessment for insurance claims, automotive repairs, and vehicle inspections without requiring manual expertise.

---

## Problem Statement

Manual car damage assessment faces several critical challenges:
- Variations in lighting, angles, and vehicle positions make visual inspection subjective and inconsistent
- Traditional assessments by inspectors are time-consuming, prone to human error, and lack standardization
- Delays in claims processing and resale evaluations due to manual inspection workflows
- Need for an automated, objective system that can classify vehicle damage reliably across diverse car images

This deep learning-based approach enables scalable, fast, and repeatable assessments, reducing processing times and improving accuracy in estimating repair costs and validating insurance claims.

---

## Dataset Overview

The dataset consists of approximately 2,300 labeled images of vehicles, carefully collected to capture various types of front and rear damage scenarios.

**Dataset Distribution:**
- Front Breakage (FB): 500 images
- Front Crushed (FC): 400 images
- Front Normal (FN): 500 images
- Rear Breakage (RB): 300 images
- Rear Crushed (RC): 300 images
- Rear Normal (RN): 300 images

Images are captured under different lighting conditions, angles, and backgrounds, with a focus on third-quarter front or rear views to mimic real-world scenarios encountered during insurance inspections or resale evaluations.

---

## Data Preprocessing

- Image Transformations (Data Augmentation & Standardization)
- Data Splitting
- Data Loaders

---

## Model Development & Optimization

- Baseline CNN Model
- Regularization Techniques Applied
- EfficientNet-B0 Implementation
- Adoption of ResNet50 Architecture
- Hyperparameter Tuning with Optuna

---

## Model Evaluation

- Classification Report
- Confusion Matrix

---

## Streamlit App Integration

---

## Live Demo

Try the application here: **[Vehicle_Damage_Detector](https://vehicle-damage-classifier.streamlit.app/)**

---

## Project Structure

```
Car_Damage_Detector/
├── model/ 
│   └── saved_model.pth        # Trained ResNet50 weights 
├── app.py                     # Streamlit app logic
├── damage_prediction.ipynb    # End-to-end notebook    
├── model_helper.py            # Prediction logic using model 
├── requirements.txt           # Required Python libraries 
├── LICENSE                    # Apache 2.0 license 
├── Car-Damage-Detector-Presentation.pdf # PDF project presentation 
└── README.md                  # Project documentation
```

---

## How to Run Locally

### Prerequisites
- Python 3.8+

### Clone the Repository
```bash
git clone https://github.com/vaibhavgarg2004/Car-Damage-Detector.git
cd Car-Damage-Detector
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
```bash
streamlit run app.py
```

---

## Technologies Used

- **Deep Learning Framework**: PyTorch
- **Model Architecture**: ResNet50 (pre-trained on ImageNet)
- **Hyperparameter Optimization**: Optuna
- **Web Framework**: Streamlit
- **Image Processing**: torchvision, PIL
- **Data Science**: NumPy, Pandas, Matplotlib

---
---

## Results Summary

- Built a deep learning system to detect and classify car damage from images into six categories: Front/Rear – Normal, Breakage, Crushed
- Prepared a dataset of 2,300 images with augmentations for better generalization
- Split dataset into 75% training and 25% validation sets, ensuring balanced class representation
- Trained baseline CNN, EfficientNet-B0, and ResNet50 with batch normalization, dropout, and L2 regularization
- Tuned ResNet50 with Optuna, achieving **77.74% final accuracy**
- Evaluated results using classification reports and confusion matrices, identifying key misclassification patterns
- Created a Streamlit app for real-time car damage classification from uploaded images
