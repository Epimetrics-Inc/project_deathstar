from rest_framework import serializers

from api.utils import QueryFieldsMixin
from .models import Document, Label

class StringListField(serializers.ListField):
    child = serializers.CharField(required=False)


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        exclude = ('document', 'created', 'modified')


class DocumentListSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    label = LabelSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('pk', 'title', 'date', 'subject','sign', 'doctype',
                  'docnum', 'label', 'created', 'modified',
                  'label__mnchn_score', 'label__specpop_score',
                  'label__geriatric_score', 'label__adolescent_score')


class DocumentGetSerializer(serializers.ModelSerializer):
    label = LabelSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('pk', 'title', 'date', 'sign', 'signtitle', 'doctype',
                  'docnum', 'label', 'created', 'modified', 'body', 'raw_body', 'label')


class VisualizationPostSerializer(serializers.Serializer):
    document_ls_one = StringListField(allow_empty=True, default=None)
    document_ls_two = StringListField(allow_empty=True, default=None)
    theme_one = serializers.CharField(max_length=15, required=False)
    theme_two = serializers.CharField(max_length=15, required=False)
    task_id = serializers.CharField(max_length=100, required=False)

    # html_output = serializers.FilePathField(path='/vagrant/core/generated/', default='')

    def validate(self, data):
        """
        Check that document references aren't the same.
        :return:
        """

        themes = ['mnchn', 'adolescent', 'geriatric', 'specpop']

        A = data.get('theme_one', None) is None
        B = data.get('theme_two', None) is None
        C = data.get('document_ls_one', None) is None
        D = data.get('document_ls_two', None) is None


        if not A and not B:
            if data['theme_one'].lower() == data['theme_two'].lower():
                raise serializers.ValidationError('Provided themes should not be the same.')
            elif not data['theme_one'].lower() in themes or not data['theme_two'].lower() in themes:
                raise serializers.ValidationError('Provided themes are not found.')

            data['type'] = 'theme'

        elif not C and not D:
            if set.intersection(set(data.get('document_ls_one', None)),
                                set(data.get('document_ls_two', None))):
                raise serializers.ValidationError('Provided documents lists have similar values.')

            try:
                # Constanly hits the DB! Maybe use a Cuckoo filter here.
                data['doc_ls_one_id'] = [Document.objects.get(title=doc).pk
                                                for doc in data['document_ls_one']]
                data['doc_ls_two_id'] = [Document.objects.get(title=doc).pk
                                                for doc in data['document_ls_two']]
                data['type'] = 'document_list'

            except Exception as e:
                raise serializers.ValidationError('Documents not found: ' + str(e))

        else:
            raise serializers.ValidationError('Provided documents or themes are insufficient.')

        return data


class VisualizationGetSerializer(serializers.Serializer):
    task_id = serializers.CharField(max_length=100, default='')
    task_status = serializers.CharField(max_length=100, default='')
    filename = serializers.CharField(max_length=100, default='')
