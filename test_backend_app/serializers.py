from django.forms import CharField
from rest_framework import serializers
from test_backend_app.models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id',
                  'name',
                  'description',
                  'toy_category',
                  'was_included_in_home')