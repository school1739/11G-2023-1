# https://colab.research.google.com/drive/18HnEw0MM1yuASoQqZH4VMnYlF07ltLHf

import pandas as pd
import numpy as np

dataset = pd.read_csv('content/IGN_reviews.csv')
dataframe = pd.DataFrame(dataset)

dataframe

dataframe.head()

dataframe.tail()

dataframe.info()

dataframe.isnull().sum()

new_dataframe = dataframe.dropna()
new_dataframe.to_csv('reviews_non-nulled.csv')