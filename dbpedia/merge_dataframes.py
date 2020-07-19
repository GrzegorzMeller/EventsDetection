import pandas as pd

hist = pd.read_pickle("hist_test.pkl")
nonhist = pd.read_pickle("non_hist_test.pkl")
frames = [hist, nonhist]
result = pd.concat(frames)
result.to_pickle("test_wiki.pkl")