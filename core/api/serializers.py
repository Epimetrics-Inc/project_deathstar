from rest_framework import serializers

from .models import Document, Label

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        exclude = ('document', 'created', 'modified')


class DocumentListSerializer(serializers.ModelSerializer):

    label = LabelSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'title', 'date', 'sign', 'doctype',
                  'docnum', 'label', 'created', 'modified', )


class DocumentGetSerializer(serializers.ModelSerializer):

    label = LabelSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'title', 'date', 'sign', 'signtitle','doctype',
                  'docnum', 'label', 'created', 'modified', 'body', 'raw_body', 'label')
