from rest_framework import serializers
from . import models

class AccountSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = models.InstagramAccounts
        fields = '__all__'
