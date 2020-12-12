from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


PROFESSIONAL = (
        ('Data Analyst', 'Data Analyst'),
        ('Python Developer', 'Python Developer'),
        ('FullStack Developer', 'FullStack Developer')
    )

TECHNOLOGIES = (
        ('API Rest', 'API Rest'),
        ('Bot', 'Bot'),
        ('Django', 'Django'),
        ('HTML', 'HTML'),
        ('Java', 'Java'),
        ('R', 'R'),
        ('React', 'React'),
        ('Webscrap', 'Webscrap')
)

class Post(models.Model):
    name = models.CharField(max_length= 255)
    slug = models.SlugField('Atalho')
    summary = models.CharField(max_length= 200) #RichTextField()
    technology = MultiSelectField(choices=TECHNOLOGIES)
    image = models.ImageField(upload_to='media', verbose_name='Imagem', default= 'media/core/images/no_preview.png')
    link = models.URLField('GitHub', blank=False)
    website = models.URLField('Website', blank=True)
    created_at = models.DateField('Updated at', auto_now_add=True)
    stack = MultiSelectField(choices=PROFESSIONAL)


    def __str__(self):
        return self.name



