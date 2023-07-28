
from django.contrib.auth.models import UserManager


class UserAccountManager(UserManager):

    def get_user_id(self, pk):
        return self.get(pk=pk)