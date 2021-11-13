from django.db.models import fields
from rest_framework import serializers
from .models import *

class LaptopAllSeriaLizers(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ("name","color","user")
