from dataclasses import field
from pyexpat import model
from rest_framework import serializers 
from shop.models import *

class Author(serializers.ModelSerializer):
    class Meta: 
        model = Author
        field = ('id','name','biography')
