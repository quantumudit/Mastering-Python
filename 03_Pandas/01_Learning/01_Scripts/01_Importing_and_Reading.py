
# IMPORTING AND READING DATASETS #
# ============================== #

"""
The basic importing and reading the dataset includes:

1. importing the library and the dataset
2. viewing the dimension of the data and top/bottom-n results with `head(n)` and `tail(n)` functions
3. viewing data with all the columns displayed
4. Viewing all the columns present in the dataset
5. Viewing basic info about the dataset with `info()` method

"""


import pandas as pd

# reading from csv file:

data = pd.read_csv('../00_Datasets/Movies_Income_Data.csv')
print(data)

# View first 10 rows of data:

print(data.head(10))


# View the dimension of the dataset (rows and columns):

print(data.shape)


# Viewing all the columns present

pd.set_option('display.max_columns', 18)
print(data.head(5))

# Getting all the column names:

cols = list(data.columns)
print(cols)

# View brief info about dataset:

print(data.info())