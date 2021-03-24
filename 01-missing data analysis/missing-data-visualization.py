# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:14:06 2021

@author: acer
"""

###############################################################################
###############################################################################
# importing required libraries
import pandas as pd
#import numpy as np
import os

#import matplotlib.pyplot as plt

###############################################################################
###############################################################################

print(os.getcwd())  # Prints the current working directory
path="C:/Users/acer/OneDrive/Documents/GitHub/data-preprocessing/01-missing data analysis"
os.chdir(path)

###############################################################################

DATA_DIR = "data" # indicate magical constansts (maybe rather put it on the top of the script)
md_filename = "melb_data.csv"# fix gruesome var names
data = pd.read_csv(os.path.join(DATA_DIR, md_filename))

###############################################################################

data.isna().sum()

###############################################################################

import missingno as msno
%matplotlib inline

msno.matrix(data)

msno.heatmap(data)

msno.bar(data)

###############################################################################