from django.db import models
from django.utils.text import slugify
# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def upload_images(instacen,imgname):

    extension = imgname.split('.')[1]
    return f'jobs_images/{instacen.id}.{extension}'
class Job(models.Model):
    title = models.CharField(max_length=100)
    # location  = 
    job_type = models.CharField(max_length=100,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published  = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    img = models.ImageField(upload_to=upload_images,default='default.jpg')

    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug= slugify(self.title)
        super(Job,self).save(*args, **kwargs)



class Category(models.Model):
    name  = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='Apply_job' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=250)
    website = models.URLField()
    cv =  models.FileField( upload_to='Apply')
    cover_letter = models.TextField(max_length=300)


    def __str__(self):
        return self.name

