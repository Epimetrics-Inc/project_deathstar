from celery import shared_task

@shared_task
def add(x, y):
    return x+y

@shared_task
def viz_scattertext(doc1, doc2):
    import scattertext as st
    import spacy
    output_fn = doc1+'_'+doc2+'.html'
    convention_df = st.SampleCorpora.ConventionData2012.get_data()
    nlp = spacy.en.English()
    corpus = st.CorpusFromPandas(convention_df,
                                    category_col = 'party',
                                    text_col = 'text',
                                    nlp = nlp).build()
    html = st.produce_scattertext_explorer(corpus,
              category='democrat',
              category_name='Democratic',
              not_category_name='Republican',
              width_in_pixels=1000,
              metadata=convention_df['speaker'])
    open('/vagrant/core/generated/'+output_fn, 'wb').write(html.encode('utf-8'))
    return output_fn
