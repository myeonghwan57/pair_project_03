from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    sectors = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=30)
    glade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    characteristic = models.CharField(max_length=50)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                format='JPEG',
    )
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 240)],
                                format='JPEG',
                                options={'quality': 100})
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Review(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                format='JPEG',
    )