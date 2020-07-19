# Historical Event Detection From Text

This experiment aims at creating good model (trained on the self-made Wikipedia dataset using DBpedia Api and ontologies) for detecting if text contains historical event or not. \
Most scripts are used for Wikipedia articles retrieval and creating dataset. In the data folder there are attached zip files with ready to use 
datasets that can be directly uploaded to Colab/Jupyter notebooks for training the LSTM network model and evaluations. \
Files description: \
All .py files aim to retrieve Wikipedia abstracts and save them to the csv file by retrieving historical articles (articles describing historical event) then non-historical and merging them. Then csv files are created, first for training, second for testing (evaluation).\
Wiki_Historical_Event_Detection.ipynb - training LSTM model and evaluating on the test set

