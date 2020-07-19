# Named Entity Recognition on the HISTO dataset

This experiment aims at creating good model (trained on the HISTO dataset) for performing NER tasks, tagging historical information in text. \
Most scripts are used for HISTO data preprocessing and creating GloVe set. In the data folder there is attached zip file with ready to use 
data that can be directly uploaded to Colab/Jupyter notebooks for training the LSTM network model and evaluations. \
Files description: \
histo_processing - preprocessing data and running CRF classifier \
data_prepeocessing_lstm.py - preprocess BIO data to the needed format for LSTM network \
bulid_glove.py and build_vocab.py and glove.py - builds necessary datasets for LSTM network \
NER_LSTM.ipynb - implementation of the LSTM network model in Tensorflow by  Guillaum Genthail (https://github.com/guillaumegenthial/tf_ner). Due to the problems with installation of Tensorflow on own PC, code is moved to the Google Colab that retrieves zip file from Google Drive and saves the model in the Google Drive  \
NER_LSTM_EVALUATION.ipynb - takes any sentence and outputs predictions \
evaluate_predictions.py - takes the output file of NER_LSTM.ipynb and evaluates precision, recall and f1 score

