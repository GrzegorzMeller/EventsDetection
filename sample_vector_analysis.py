import numpy as np
from glove import load_word2vec
from glove import convert_to_pandas_remove_stopwords
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd


def get_vectors(model):
    """as an input provide word2vec"""
    vocab = list(model.vocab)
    X = model[vocab]
    tsne = TSNE(random_state=25111993, n_components=2)
    X_tsne = tsne.fit_transform(X)
    positions = pd.DataFrame(X_tsne, columns=['x', 'y'])
    words = pd.DataFrame(vocab, columns=['word'])
    df = pd.concat([words, positions], axis=1)
    return  df


def plot_vectors(model1, model2, word):
    """as an input provide pandas dataframe with 2 dimensions for vector position"""
    vec1 = model1.iloc[model1[model1["word"] == word].index.values[0], 1:3].to_numpy()
    vec2 = model2.iloc[model2[model1["word"] == word].index.values[0], 1:3].to_numpy()
    print(vec1[0], vec2)

    ax = plt.axes()
    ax.arrow(0.0, 0.0, vec1[0], vec1[1], head_width=0.5, head_length=0.7, fc='blue', ec='blue')
    ax.arrow(0.0, 0.0, vec2[0], vec2[1], head_width=0.5, head_length=0.7, fc='green', ec='green')
    plt.grid()

    plt.xlim(-250, 250)
    plt.ylim(-250, 250)

    plt.show()


if __name__ == "__main__":
    glove_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt", 100)
    vec1 = get_vectors(glove_model)
    print(vec1)

    levy_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\levy\\HistoLevy.txt", 100)
    vec2 = get_vectors(levy_model)

    plot_vectors(vec1, vec2,"will")

    #V = np.array([vec1[0], vec2[0]])
    #origin = [0], [0]  # origin point

    #plt.quiver(*origin, V[:, 0], V[:, 1], color=['r', 'b', 'g'], scale=21)
    #plt.show()