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
            return 'https://picsum.photos/200/200'
