from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors
from gensim import models
import numpy as np
from sklearn.manifold import TSNE
from  sklearn.metrics.pairwise import cosine_similarity
from  sklearn.metrics.pairwise import cosine_distances
import matplotlib.pyplot as plt
import pandas as pd
from stop_words import get_stop_words

def convert_to_word2vec():
    glove2word2vec(glove_input_file="D:\\projects\\inf_retrieval\\datasets\\glove\\glove.6B.300d.txt",
              word2vec_output_file="D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt")


def load_word2vec(file_path ,lim):
    glove_model = KeyedVectors.load_word2vec_format(
        file_path, binary=False, limit=lim)

    return glove_model


def compare_simmilar(w, model):
    """as an input provide word2vec"""
    print(model.most_similar(w))


def convert_to_pandas_remove_stopwords(model):
    """as an input provide word2vec"""
    vocab = list(model.vocab)
    stop_words = list(get_stop_words('en'))
    punctuation = ['</s>', '@', ',', '.', "''", ';', '--', "'", '!', "n't", '?', '#', '"', '(', ')', '[', ']', '~', '-', "'s", "'m", "'re", '/']
    to_remove = []
    for q in vocab:
        if q in stop_words or q in punctuation:
            to_remove.append(q)
    for e in to_remove:
        vocab.remove(e)
    pos = model[vocab]
    positions = pd.DataFrame(pos)
    words = pd.DataFrame(vocab, columns=['word'])
    df = pd.concat([words, positions], axis=1)
    return df


def plot_wor2vec(model):
    """as an input provide pandas word2vec"""
    vocab = list(model.wv.vocab)
    print(vocab)
    X = model[vocab]
    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)
    positions = pd.DataFrame(X_tsne, columns=['x', 'y'])
    words = pd.DataFrame(vocab, columns=['word'])
    df = pd.concat([words, positions], axis=1)
    df['word'] = df['word'].astype(str)
    print(df)
    # plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df['x'], df['y'])
    for q in df.index:
        ax.annotate(df['word'][q], (df['x'][q], df['y'][q]))
    plt.show()


def compare_models(model1, model2):
    """as an input provide two pandas dataframes"""
    df = pd.DataFrame(columns=["word", "distance"])
    for q in model1.index:
        if model1["word"][q] in model2["word"].values:
            vec1 = model1.iloc[q, 1:302].to_numpy()
            vec1 = vec1.reshape(1, 300)
            vec2 = model2.iloc[model2[model2["word"] == model1["word"][q]].index.values[0], 1:302].to_numpy()
            vec2 = vec2.reshape(1, 300)
            dist = cosine_distances(vec1, vec2)
            df = df.append({"word": model1["word"][q],
                              "distance": dist[0][0]}, ignore_index=True)

    print(df)

if __name__ == "__main__":
    glove_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt", 150) #lim=200000
    glove_no_stopwords = convert_to_pandas_remove_stopwords(glove_model)

    levy_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\levy\\HistoLevy.txt", 150) #lim=78041
    levy_no_stopwords = convert_to_pandas_remove_stopwords(levy_model)

    compare_models(levy_no_stopwords, glove_no_stopwords)

    #plot_wor2vec(levy_model)
    #compare_simmilar("girl", glove_model)

