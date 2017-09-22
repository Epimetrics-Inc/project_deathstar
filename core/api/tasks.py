from celery import shared_task
from django.conf import settings

@shared_task
def viz_scattertext(ids, task_type):
    import os

    if settings.DEBUG:
        dir = '/vagrant/core/generated/'
    else:
        dir = None

    if task_type == 'document_list':
        id1 = ids[0][0]
        id2 = ids[1][0]
    else:
        id1 = ids[0]
        id2 = ids[1]

    id1 = str(id1)
    id2 = str(id2)

    existing = False
    fn = []
    for _, _, f in os.walk(dir):
        fn += f

    output_fn = id1 + '_' + id2 + '.html'

    if id1 + '_' + id2 + '.html' in fn:
        existing = True
    elif id2 + '_' + id1 + '.html' in fn:
        existing = True
        output_fn = id2 + '_' + id1 + '.html'


    # if not existing:
    #     from api.models import Document
    #     # Document.objects.get(title=doc1)
    #     res = create_scattertext(doc1, doc2, dir+output_fn)

    return output_fn
