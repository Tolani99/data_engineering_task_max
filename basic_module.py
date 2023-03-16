"""
To conduct the analysis and answer the questions,
we can use Python and its data analysis libraries such as Pandas,
Numpy, and Matplotlib.
Let's start by importing the necessary libraries and loading the dataset.
"""
# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load the data into a pandas dataframe
df = pd.read_csv('placements_data.tsv', sep='\t')

# Write the CSV file
df.to_csv('placements_data.csv', index=False)

# Display the first few rows
# print(df.head())

