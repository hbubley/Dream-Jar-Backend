from rest_framework import serializers
from apps.dreamjarmaker.models import Dream


class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ('dream', 'completed')