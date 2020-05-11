from glove import load_word2vec
from glove import compare_simmilar


if __name__ == "__main__":
    levy_model = load_word2vec("D:\\projects\\inf_retrieval\\datasets\\levy\\HistoLevy.txt", 78000)
    compare_simmilar(levy_model, "location")
