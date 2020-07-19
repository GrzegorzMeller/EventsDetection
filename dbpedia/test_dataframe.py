import pandas as pd

unpickled_df = pd.read_pickle("non_hist_test.pkl")
print(unpickled_df.shape)
print(unpickled_df.iloc[222])
print(unpickled_df.iloc[500].Name)
print(unpickled_df.iloc[500].Abstract)
