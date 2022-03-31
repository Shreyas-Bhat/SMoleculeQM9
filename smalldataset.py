# -*- coding: utf-8 -*-
"""SmallDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hj7OoZXQm6FShS-dxrHn0ymkR4-WitGV
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd

qm9 = pd.read_csv('/content/drive/MyDrive/QM9 resources/data/qm9.csv')

qm9.head(-10)

qm9.shape

qm9_small = pd.DataFrame()

qm9.iloc[[0]]

for i in range(0, int((qm9.shape[0])), 10):
    # print(i)
    x = int(np.random.uniform(i, i+10))
    # print(x)
    entry = qm9.iloc[x]
    print([entry])
    qm9_small = qm9_small.append([entry])

qm9_small

qm9_small.to_csv('qm9_small.csv')
