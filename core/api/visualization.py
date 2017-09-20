import scattertext as st
import spacy


def create_scattertext(corpus_1_df, corpus_2_df, output_fn):
    df = corpus_1_df.append(corpus_2_df)
    labels = df['label'].unique()
    #
    # convention_df = st.SampleCorpora.ConventionData2012.get_data()
    nlp = spacy.en.English()
    corpus = st.CorpusFromPandas(df,
                                 category_col='label',
                                 text_col='text',
                                 nlp=nlp).build()
    html = st.produce_scattertext_explorer(corpus,
                                           category=labels[0],
                                           category_name=labels[0],
                                           not_category_name=labels[1],
                                           width_in_pixels=1000)
    open(output_fn, 'wb').write(html.encode('utf-8'))
    return True
