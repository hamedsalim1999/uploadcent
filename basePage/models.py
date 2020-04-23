from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class Post(models.Model):
    uid = models.UUIDField(primary_key= True , default= uuid.uuid4 , editable=False)
    tittle = models.CharField(max_length=256, db_index=True ,unique_for_date='published_at' )
    published_at = models.DateTimeField(default = timezone.now)
    main_text = models.TextField()
    image = models.ImageField(upload_to='post',blank=True, null=True , help_text='uplaod image',width_field='width_field', height_field='height_field')
    width_field  = models.PositiveIntegerField(null = True , blank = True , default = '1080')
    height_field = models.PositiveIntegerField(null = True , blank = True , default = '720')
    main_file = models.FileField(upload_to='resume_file',blank=True, null=True)