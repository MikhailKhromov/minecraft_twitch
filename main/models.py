import secrets

import requests
from django.db import models
import pysftp
from django.db.models.signals import post_save


class Player(models.Model):
    twitch_id = models.CharField(max_length=30, unique=True)
    mc_username = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.twitch_id) + '; ' + str(self.mc_username)


def edit_whitelist(sender, instance, **kwargs):
    if not kwargs['created']:
        url = 'http://auth.wingedproject.ru/panel/easywladd.php'
        requests.post(url, data={'username': instance.mc_username,
                                 'user': secrets.user, 'hash': secrets.hash})


post_save.connect(edit_whitelist, sender=Player)
