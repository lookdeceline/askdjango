from django.db import models
import re
from django.forms import ValidationError
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*)/[+-]?(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    author = models.CharField(max_length=20) #blank, null options False by default
    title = models.CharField(max_length=100, help_text="title of article") # verbose_name = "제목"
    content = models.TextField() # verbose_name = "내용"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    tags = models.CharField(max_length=100, blank = True)
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              help_text= "위도/경도 형식으로 입력", blank = True)


