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
        file_path, binary=False, limit=1000)

    return glove_model


def compare_simmilar(w, model):
    print(model.most_similar(w))


def plot_wor2vec(model):
    vocab = list(model.wv.vocab)
    X = model[vocab]
    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)
    positions = pd.DataFrame(X_tsne, columns=['x', 'y'])
    words = pd.DataFrame(vocab, columns=['word'])
    df = pd.concat([words, positions], axis=1)
    df['word'] = df['word'].astype(str)
    print(df)

    # remove stopwords from the dataframe
    stop_words = list(get_stop_words('en'))
    df = df[~df["word"].isin(stop_words)]
    print(df)

    # plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df['x'], df['y'])
    for q in df.index:
        ax.annotate(df['word'][q], (df['x'][q], df['y'][q]))
    plt.show()

if __name__ == "__main__":
    glove_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt")
    plot_wor2vec(glove_model)
    #compare_simmilar("girl", glove_model)

