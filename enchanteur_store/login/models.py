from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    zip_code = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(null=True)
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()

models.signals.post_save.connect(create_profile, sender=User)
models.signals.post_save.connect(save_profile, sender=User)
