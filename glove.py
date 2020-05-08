from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors
from gensim import models
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd
from stop_words import get_stop_words

def convert_to_word2vec():
    glove2word2vec(glove_input_file="D:\\projects\\inf_retrieval\\datasets\\glove\\glove.6B.300d.txt",
              word2vec_output_file="D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt")


def load_word2vec(file_path):
    glove_model = KeyedVectors.load_word2vec_format(
        file_path, binary=False, limit=78000)

    return glove_model


def compare_simmilar(w, model):
    """as an input provide word2vec"""
    print(model.most_similar(w))


def convert_to_pandas_remove_stopwords(model):
    """as an input provide word2vec"""
    vocab = list(model.vocab)
    stop_words = list(get_stop_words('en'))
    punctuation = ['</s>', '@', ',', '.', "''", ';', '--', "'", '!', "n't", '?', '#', '"', '(', ')', '[', ']', '~', '-', "'s"]
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


if __name__ == "__main__":
    #glove_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt")
    #plot_wor2vec(glove_model)

    levy_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\levy\\HistoLevy.txt")
    print(levy_model)
    levy_no_stopwords = convert_to_pandas_remove_stopwords(levy_model)
    print(levy_no_stopwords)
    #plot_wor2vec(levy_model)
    #compare_simmilar("girl", glove_model)

