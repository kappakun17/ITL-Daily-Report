from django.db import models
from user.models import User
import uuid , os

# Create your models here.

def image_directory_path(instance, filename):
    re_uuid_user_id = str(uuid.uuid5(uuid.uuid1(), str(instance.id))).replace('-','')
    re_uuid_filename = str(uuid.uuid5(uuid.uuid1(), str(os.path.splitext(filename)))).replace('-','')
    index = filename.index('.')
    extention = filename[index:]
    
    export_filename = re_uuid_filename + extention

    return 'profile_images/{}/{}'.format(re_uuid_user_id,export_filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hobby = models.CharField('hobby',max_length=250)
    introduction = models.TextField('introduction',max_length=300)
    user_image = models.ImageField(verbose_name='user_image',upload_to=image_directory_path, default='profile-images/default/user.png')