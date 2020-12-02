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
    summary = RichTextField()
    technology = MultiSelectField(choices=TECHNOLOGIES)
    image = models.ImageField(upload_to='core/images', verbose_name='Imagem', null=True, blank=True)
    link = models.URLField('GitHub', blank=False)
    website = models.URLField('website', blank=True)
    created_at = models.DateField('Updated at', auto_now_add=True)
    stack = MultiSelectField(choices=PROFESSIONAL)


    def __str__(self):
        return self.name



