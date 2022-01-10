import pandas as pd
import numpy as np

dataset = pd.read_csv("IGN_reviews.csv")

dataframe = pd.DataFrame(dataset)
print(dataframe)

dataframe.head(1)

dataframe.tail(2)

dataframe.info()

dataframe = dataframe.isnull()

dataframe.sum()

new_dataframe = dataframe.dropna()

new_dataframe.to_csv("non-nulled.csv")