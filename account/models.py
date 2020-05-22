from django.db import models
from django.conf import settings

# Create your models here.
class UserReg(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    mobile_num=models.BigIntegerField(unique=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
