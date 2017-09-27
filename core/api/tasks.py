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
        id1 = sorted(ids[0])
        id2 = sorted(ids[1])
    elif task_type == 'theme':
        id1 = ids[0]
        id2 = ids[1]
    else:
        raise RuntimeError('Unknown task type %s !' % task_type)

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

    if not existing:
        from api.models import Document
        import pandas as pd
        from api.visualization import create_scattertext

        df = pd.DataFrame()

        if task_type == 'theme':
            theme_one = [i.body for i in Document.objects.order_by('-label__'+id1+'_score')[:100]]
            theme_two = [i.body for i in Document.objects.order_by('-label__'+id2+'_score')[:100]]
            df['text'] = theme_one + theme_two
            df['label'] = [id1 for i in range(100)] + [id2 for i in range(100)]

        else:
            doc_one = [Document.objects.get(pk=id).body for id in id1]
            doc_two = [Document.objects.get(pk=id).body for id in id2]
            df['text'] = doc_one + doc_two
            df['label'] = ['Group 1' for i in range(len(doc_one))] + ['Group 2' for i in range(len(doc_two))]

        res = create_scattertext(df, dir+output_fn)

    return output_fn
