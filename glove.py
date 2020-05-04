from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors

#glove2word2vec(glove_input_file="D:\\projects\\inf_retrieval\\datasets\\glove\\glove.6B.300d.txt",
#               word2vec_output_file="D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt")

glove_model = KeyedVectors.load_word2vec_format("D:\\projects\\inf_retrieval\\datasets\\glove\\gensim_glove_vectors.txt", binary=False, limit=78000)
#print(glove_model["beautiful"])
print(glove_model.most_similar("girl"))

hist_levy_model = KeyedVectors.load_word2vec_format("D:\\projects\\inf_retrieval\\datasets\\levy\\HistoLevy.txt", binary=False, limit=78000)
print(hist_levy_model.most_similar("girl"))