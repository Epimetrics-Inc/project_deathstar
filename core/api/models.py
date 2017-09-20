from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import OneToOneField
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


class Label(ext_models.TimeStampedModel):
    document = OneToOneField(
        Document,
        on_delete=models.CASCADE,
        primary_key=True
    )

    default_params = {
        'decimal_places': 2,
        'max_digits': 4,
        'default': 0
    }

    mnchn_score = models.DecimalField(**default_params)
    adolescent_score = models.DecimalField(**default_params)
    spec_pop_score = models.DecimalField(**default_params)
    geriatric_score = models.DecimalField(**default_params)

    def __str__(self):
        return "%s \n mnchn: %s \n adolescent: %s \n" \
               "spec_pop: %s \n geriatric: %s \n" \
               % (self.document, self.mnchn_score, self.adolescent_score,
                  self.spec_pop_score, self.geriatric_score)
