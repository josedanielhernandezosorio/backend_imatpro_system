from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from com.sofyntelligen.imatpro.app.backend.account.manager import UserAccountManager


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    objects = UserAccountManager()

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return 'https://api.dicebear.com/6.x/initials/svg?seed=' + self.first_name + '&backgroundColor=b6e3f4,c0aede,d1d4f9,ffd5dc'
