# -*- coding: utf-8 -*-
"""Pack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MjA8oPVUM9ciWOL6IXj9OCFyrZ2Fk4si
"""

import numpy as np
import pandas as pd
!pip install -U scikit-learn
!pip install psycopg2-binary
import sqlalchemy as sqla
from scipy import stats
import matplotlib

x = np.random.rand(100)
x

a = np.mean(x)
a

b = np.median(x)
b

c = stats.mode(x)
c

d = np.std(x)
d

e = np.var(x)
e
