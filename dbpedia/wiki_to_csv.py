import pandas as pd

hist = pd.read_pickle("test_wiki.pkl")
hist.to_csv('test_wiki.csv', header=True)