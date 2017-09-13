from rest_framework import serializers

from .models import Document


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'date', 'sign', 'doctype',
                  'docnum', 'created', 'modified', 'body',)


class DocumentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
