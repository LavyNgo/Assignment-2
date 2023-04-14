# import some necessary libraries
import os
import pandas as pd

# create path for local
path_in = r'C:\Users\Lavy Ngo\Desktop\CS5530\Assignment2\diabetes.csv'
path_out = r'C:\Users\Lavy Ngo\Desktop\CS5530\Assignment2\clean_data.csv'

# read data from a raw file
# data = pd.read_csv('/content/raw_human_data.csv')
data = pd.read_csv(path_in)

print(data)
