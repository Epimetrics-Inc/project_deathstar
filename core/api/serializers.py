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


class VisualizationPostSerializer(serializers.Serializer):
    document_one = serializers.CharField(max_length=15)
    document_two = serializers.CharField(max_length=15)
    task_id = serializers.CharField(max_length=100, default='')
    # html_output = serializers.FilePathField(path='/vagrant/core/generated/', default='')

    def validate(self, data):
        """
        Check that document references aren't the same.
        :return:
        """
        if data['document_one'] == data['document_two']:
            raise serializers.ValidationError("Provided documents should not be the same.")
        return data

class VisualizationGetSerializer(serializers.Serializer):
    task_id = serializers.CharField(max_length=100, default='')
    task_status = serializers.CharField(max_length=100, default='')
    filename = serializers.CharField(max_length=100, default='')
