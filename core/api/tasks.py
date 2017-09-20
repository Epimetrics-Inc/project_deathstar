from celery import shared_task


@shared_task
def viz_scattertext(doc1, doc2):
    import os

    dir = '/vagrant/core/generated/'

    existing = False
    fn = []
    for _, _, f in os.walk(dir):
        fn += f

    if doc1 + '_' + doc2 + '.html' in fn or doc2 + '_' + doc1 + '.html' in fn:
        existing = True

    output_fn = doc1 + '_' + doc2 + '.html'

    # if not existing:
    #     from api.models import Document
    #     # Document.objects.get(title=doc1)
    #     res = create_scattertext(doc1, doc2, dir+output_fn)

    return output_fn
