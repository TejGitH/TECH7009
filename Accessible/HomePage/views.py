from django.shortcuts import render
import cv2
import os
import random
import shutil
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense
#from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import ImageDataGenerator
import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.utils import Sequence


# Create your views here.

def home(request):
    return render(request, "HomePage/index.html")

class CustomImageDataGenerator(Sequence):

    # Define your dataset paths and parameters
    edge_image_folder = 'C:/Users/gteja/Documents/Tejal docs/OBU - SEM3/Code/Dataset/newcanny 5'
    annotation_folder = 'C:/Users/gteja/Documents/Tejal docs/OBU - SEM3/Code/Dataset/label5'
    batch_size = 32
    target_size = (512, 256)
    num_classes = 15

    def __init__(self, edge_image_folder, annotation_folder, batch_size, target_size, num_classes):
        self.edge_image_folder = edge_image_folder
        self.annotation_folder = annotation_folder
        self.batch_size = batch_size
        self.target_size = target_size
        self.num_classes = num_classes

        # Load edge images and annotations
        self.edge_detected_images, self.annotations = self.load_data()

    def load_data(self):
        edge_detected_images = []

        annotations = []

        for image_filename in os.listdir(self.edge_image_folder):
            if image_filename.endswith(".png"):
                image_path = os.path.join(self.edge_image_folder, image_filename)
                edge_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                edge_detected_images.append(edge_image)

                # Load corresponding annotation (modify this part based on your annotation format)
                annotation_filename = os.path.splitext(image_filename)[0] + '.xml'
                annotation_path = os.path.join(self.annotation_folder, annotation_filename)
                annotation_info = self.parse_annotation(annotation_path)
                annotations.append(annotation_info)

        return edge_detected_images, annotations

    def parse_annotation(self, annotation_path):
        # Parse the XML file (adjust this part based on your annotation format)
        tree = ET.parse(annotation_path)
        root = tree.getroot()

        # Extract information from the XML as needed
        # For example, if your XML contains object annotations, you can iterate through them
        for obj in root.findall('object'):
            class_label = obj.find('name').text  # Extract class label
            bbox = obj.find('bndbox')  # Extract bounding box coordinates
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)

            # Store the extracted information in a suitable data structure
            annotation_info = {
                'class_label': class_label,
                'bbox': (xmin, ymin, xmax, ymax)
            }

            return annotation_info

    def __len__(self):
        return int(np.ceil(len(self.edge_detected_images) / self.batch_size))

    def __getitem__(self, idx):
        batch_edge_images = self.edge_detected_images[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_annotations = self.annotations[idx * self.batch_size:(idx + 1) * self.batch_size]

        X = np.zeros((len(batch_edge_images), *self.target_size, 1))
        Y = np.zeros((len(batch_edge_images), self.num_classes))

        for i, (edge_image, annotation) in enumerate(zip(batch_edge_images, batch_annotations)):
            # Load and preprocess the Canny edge-detected image
            edge_image = cv2.resize(edge_image, self.target_size)
            edge_image = edge_image / 255.0  # Normalize pixel values to [0, 1]

            # Load and preprocess annotations (modify this part according to your needs)
            # For example, you can extract object bounding boxes and class labels from annotations

            # Assign the preprocessed edge image and annotation to the batch
            X[i] = edge_image[:, :, np.newaxis]  # Add a single channel dimension
            Y[i] = annotation  # Replace with your annotation processing logic

        return X, Y




def explore(request):
    return render(request, "HomePage/explore.html")

def upload(request):
    return render(request, "HomePage/upload.html")

def chat(request):
    return render(request, "HomePage/chat.html")

def about(request):
    return render(request, "HomePage/about.html")

def accessible(request):
    return render(request, "HomePage/accessible.html")
