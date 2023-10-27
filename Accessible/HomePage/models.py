from django.db import models


class StoreImage(models.Model):
    image = models.ImageField(upload_to='uploadedImgs/')
    cannyimg = models.ImageField(default='default.png', upload_to='cannyImgs/')
    
