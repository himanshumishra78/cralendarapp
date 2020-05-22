from django.db import models
from django.conf import settings

# Create your models here.
class UserReg(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    mobile_num=models.BigIntegerField(unique=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class LoggedUser(models.Model):
    user = models.ForeignKey(User, primary_key=True)

    def __unicode__(self):
        return self.user.username

    def login_user(sender, request, user, **kwargs):
        LoggedUser(user=user).save()

    def logout_user(sender, request, user, **kwargs):
        try:
            u = LoggedUser.objects.get(user=user)
            u.delete()
        except LoggedUser.DoesNotExist:
            pass

    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)
