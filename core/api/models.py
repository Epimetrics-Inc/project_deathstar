from django.contrib.postgres.fields import JSONField
from django.db import models
from django_extensions.db import models as ext_models


class Document(ext_models.TimeStampedModel):
    title = models.TextField()
    date = models.DateField(null=True)
    doctype = models.TextField(null=True)
    docnum = models.TextField(null=True)
    subject = models.TextField(null=True)
    body = models.TextField(null=True)
    sign = models.TextField(null=True)
    signtitle = models.TextField(null=True)
    images = JSONField(null=True)
    raw_body = JSONField(null=True)

    class Meta:
        ordering = ('date', 'modified',)

    def __str__(self):
        return "%s" % (self.title)
