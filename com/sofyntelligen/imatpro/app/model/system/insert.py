from django.contrib.auth.models import User

user = User.objects.create_user('josedanielhernandezosorio', 'josedaniel.hernandez.osorio@sofyntelligen.com',
                                'Andy2509')

user.first_name = 'Jose Daniel'
user.last_name = 'Hernandez Osorio'

user.save()
