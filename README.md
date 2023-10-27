# TECH7009
# AI Platform for Visually Impaired Parents to Interpret their Children’s Drawings and Illustrations
![UICapture1](https://github.com/TejGitH/TECH7009/assets/128676595/4489b2e6-f51c-4965-9527-3b2d1b452a73)
![UICapture2](https://github.com/TejGitH/TECH7009/assets/128676595/4feb8e63-adca-40e0-b4b8-9bd736062702)
![UICapture3](https://github.com/TejGitH/TECH7009/assets/128676595/f96ed61c-53b1-4dc5-a0c9-e7c0300d3f07)
![UICapture4](https://github.com/TejGitH/TECH7009/assets/128676595/68308fa4-3034-4c4b-ad1b-244c75055d13)
![UICapture5](https://github.com/TejGitH/TECH7009/assets/128676595/f97e5794-4591-4ab8-ada6-7cab2b9dd862)
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Code](#code)

## Introduction

This is a Django-based AI platform that provides services for visually impaired users to upload their children's drawings and interpret if the image is of a person or not. They can also explore other images which will be stored in the database during the upload activity.

## Features

- Upload Images to perform object detection
- Explore images and perform object detection
- User-friendly web interface

## Technologies Used

- Django
- Computer Vision Library
- REST framework
- Tensorflow and Keras for CNN model building
- HTML/CSS for the web interface
- JavaScript (for interactive features)
- SQLite (or any compatible database)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e-commerce-chatbot.git

1. Install the required Python packages:
   
   pip install -r requirements.txt
2. Set up your database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
3.Run migrations:

-python manage.py makemigrations
-python manage.py migrate

4. Start the development server:

python manage.py runserver

## Usage
-Visit the web interface and use the services
-You can upload images
-Explore the different images.

## Dataset
https://www.kaggle.com/datasets/lachin007/drawaperson-handdrawn-sketches-by-children

## Code
views.py
