from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField('Atalho')
    summary = RichTextField()
    technology = models.TextField('Techs', blank=False)
    image = models.ImageField(upload_to='core/images', verbose_name='Imagem', null=True, blank=True)
    link = models.URLField('GitHub', blank=False)
    website = models.URLField('website', blank=True)
    created_at = models.DateField('Updated at', auto_now_add=True)

    def __str__(self):
        return self.title