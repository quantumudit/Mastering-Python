
# DATATYPE TRANSFORMATIONS #
# ====================== #

"""
The datatype transformation includes the following transformartions:

1. Viewing unique items present in a column
2. Replacing values
3. Changing datatype

"""

import pandas as pd
import numpy as np

data = pd.read_csv('../00_Datasets/Toyota.csv',na_values=["??","????"], index_col = 0)


# Viewing the datatypes and first five data:

print(data.dtypes)
print(data.head(5))

# Viewing the object datatypes only

print(data.select_dtypes(include=[object]))

# Viewing unique items in a series:

print(np.unique(data.KM))
print(np.unique(data.FuelType))
print(np.unique(data.HP))
print(np.unique(data.Doors))

# Replacing values:

data.Doors.replace("three", 3, inplace=True)
data.Doors.replace("four", 4, inplace=True)
data.Doors.replace("five", 5, inplace=True)




# Changing the datatype of a column:

# movies.profit = movies.profit.astype('float64')
# movies.title = movies.title.astype('category')
# movies.genre = movies.title.astype('category')

# print(movies.info())