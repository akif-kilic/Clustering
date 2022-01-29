# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:40:24 2021

@author: ANA-PC
"""

import pandas as pd
data=pd.read_csv("deneme.txt",sep=",",header=None)
data.columns=["arabalar","fiyat"]
import matplotlib.pyplot as plt
plt.plot(data["arabalar"],data["fiyat"], color="red")
plt.show()