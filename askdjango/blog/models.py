from django.db import models
import re
from django.forms import ValidationError
# Create your models here.
from django.urls import reverse


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*)/[+-]?(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    author = models.CharField(max_length=20) #blank, null options False by default
    title = models.CharField(max_length=100, help_text="title of article") # verbose_name = "제목"
    content = models.TextField() # verbose_name = "내용"
    photo = models.ImageField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    tags = models.CharField(max_length=100, blank = True)
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              help_text= "위도/경도 형식으로 입력", blank = True)


    class Meta:     #데이터베이스에 특정 필드로 정렬 조건 추가 lec9/26:56
                    #queryset내 기본정렬은 모델내 Meta.ordering 설정을 따름
        ordering = ['-id']   # 'id': 올림차순정렬


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.pk)])



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    #.ForeignKey()로 생성하면 SQL에서는 post_id라는 이름의 필드가 생성됨.
    author = models.CharField(max_length=20)
    message = models.TextField()
    tag_set = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)