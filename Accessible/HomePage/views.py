from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from .models import StoreImage
import base64
from io import BytesIO
import cv2
import os
import random
import shutil
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import xml.etree.ElementTree as ET
from keras import layers
from keras.utils import Sequence


# Create your views here.

def home(request):
    return render(request, "HomePage/index.html")

def is_image(file):
    try:
        with Image.open(file) as img:
            return img.format is not None
    except:
        return False

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']

        if uploaded_file:
            try:
                if is_image(uploaded_file):
                    # Get the uploaded file's name
                    uploaded_file_name = uploaded_file.name
                    #return HttpResponse({uploaded_file_name})
                    
                    # loads and read an image from path to file
                    img = cv2.imread('C:/Users/gteja/Documents/Tejal docs/OBU - SEM3/Code/Dataset/4/'+uploaded_file_name)
                    gray_image = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        # Create an instance of the Image model and set the image field
                        image_instance = StoreImage(image=uploaded_file)

                        # Save the image instance to the database
                        image_instance.save()

                        #kernel = [(15, 0)]  # (Kernel size, Sigma)
                        kernel_size = 15
                        sigma = 0                    
                        edges = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), sigma)

                        # Apply Canny edge detection
                        canny = cv2.Canny(edges, threshold1=50, threshold2=150)  # Adjust thresholds as needed
                        
                        _, ori_img_data = cv2.imencode('.jpg', img)
                        ori_img_base64 = base64.b64encode(ori_img_data).decode()

                        _, canny_img_data = cv2.imencode('.png', canny)
                        canny_img_base64 = base64.b64encode(canny_img_data).decode()

                        # Pass the image URL to the template context
                        context1 = {
                            'image_url1': 'data:image/jpg;base64,' + ori_img_base64
                        }
                        
                        # Pass the image URL to the template context
                        context2 = {
                            'image_url2': 'data:image/png;base64,' + canny_img_base64
                        }
                        merged_context = {**context1, **context2}
                        #merged_context = {context1}

                        #model_result = cnnmodel(request)

                        # Render the template with the image
                        return render(request, 'HomePage/upload.html', merged_context)
                        #return render(request, 'HomePage/upload.html', context1)
                    else:
                        return HttpResponse('Failed to process the uploaded image.')
            except Exception as e:
                    return HttpResponse(f'Error processing the image: {str(e)}')
            else:
                return HttpResponse('The uploaded file is not an image.')
        else:
            return HttpResponse('No image file was selected.')
            
    return render(request, 'index.html')


def explore_view(request):
    all_images = StoreImage.objects.all()
    return render(request, 'HomePage/explore.html', {'all_images': all_images})

class cnnmodel(Sequence):
    def get(self, request):

        # Retrieve edge-detected images from the database
        all_images = StoreImage.objects.all()
        # Create a list to store the canny field you want to access from each object
        edge_images = []

        # Loop through the StoreImage objects and access the specific field
        for obj in all_images:
            canny_field = obj.cannyimg  # Replace 'your_field_name' with the actual field name
            edge_images.append(canny_field)
        
        
        # Load annotations from a local file repository (replace with your logic)
        annotation_folder = 'C:/Users/gteja/Documents/Tejal docs/OBU - SEM3/Code/Dataset/label5'
        annotation_files = os.listdir(annotation_folder)
        annotations = {}
        for filename in annotation_files:
            #with open(os.path.join(annotation_folder, filename), 'r') as file:
            #    annotations[filename] = file.read()

            if filename.endswith('.xml'):
                xml_path = os.path.join(annotation_folder, filename)
                tree = ET.parse(xml_path)
                root = tree.getroot()
                # Parse all elements in the XML file
                annotation = {}
                for elem in root.iter():
                    annotation[elem.tag] = elem.text
                annotations[filename] = annotation


        # Combine edge images and annotations for CNN training (replace with your training logic)
        training_data = []
        for edge_image in edge_images:
            image_path = edge_image.cannyimg.path
            image_filename = os.path.basename(image_path)
            annotation = annotations.get(image_filename, {})
            training_data.append({'image_path': image_path, 'annotation': annotation})
            # Define your CNN model
        
        num_classes = 15
        model = keras.Sequential([
            # Convolutional Block 1
            layers.Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(512, 256, 1)),
            layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2)),
            
            # Convolutional Block 2
            layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
            layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2)),
            
            # Convolutional Block 3
            layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
            layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
            layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2)),
            
            # Flatten and Fully Connected Layers
            layers.Flatten(),
            layers.Dense(256, activation='relu'),
            layers.Dropout(0.5),  # Dropout layer for regularization
            layers.Dense(num_classes, activation='softmax')  # Replace 'num_classes' with the actual number of classes
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Summary of the model architecture
        model.summary() 

        # Evaluate the model on your custom data generator
        test_loss, test_accuracy = model.evaluate(custom_data_generator)
        print(f'Test Loss: {test_loss:.4f}')
        print(f'Test Accuracy: {test_accuracy:.4f}')

        # Perform CNN training with the training_data
        
        
        
        
        
        
        return render(request, 'your_template.html', {'training_data': training_data})