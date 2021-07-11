
# COLUMN TRANSFORMATIONS #
# ====================== #

"""
The column transformation includes the following transformartions:

1. Renaming columns
2. Rearranging the columns
3. Selecting specific columns
4. Viewing column stats
4. Viewing datatype of columns

"""

import pandas as pd

data = pd.read_csv('../00_Datasets/Movies_Income_Data.csv')

original_cols = [
    'Day of Week', 
    'Director', 
    'Genre', 
    'Movie Title', 
    'Release Date', 
    'Studio', 
    'Adjusted Gross ($mill)', 
    'Budget ($mill)', 
    'Gross ($mill)', 
    'IMDb Rating', 
    'MovieLens Rating', 
    'Overseas ($mill)', 
    'Overseas%', 
    'Profit ($mill)', 
    'Profit%', 
    'Runtime (min)', 
    'US ($mill)', 
    'Gross % US'
]

renamed_cols = [
    'weekday', 
    'director', 
    'genre', 
    'title', 
    'released', 
    'studio', 
    'adjusted_gross', 
    'budget', 
    'gross', 
    'imdb_rating', 
    'movielens_rating', 
    'overseas', 
    'overseas_pct', 
    'profit', 
    'profit_pct', 
    'runtime', 
    'us_revenue', 
    'gross_us_pct'
]

# Changing the column names:

data.columns = renamed_cols
print(data.head(7))

# Rearranging the columns:

renamed_cols = [
    'title', 
    'genre', 
    'studio',
    'director',
    'released',
    'weekday',
    'imdb_rating', 
    'movielens_rating', 
    'adjusted_gross', 
    'budget', 
    'gross', 
    'overseas', 
    'overseas_pct', 
    'profit', 
    'profit_pct', 
    'runtime', 
    'us_revenue', 
    'gross_us_pct'
]

data = data.reindex(columns = renamed_cols)
print(data.head(5))

# Selecting specific columns:

required_cols = [
    'title', 
    'genre',
    'released',
    'imdb_rating',
    'budget',
    'profit'
]

movies = data[required_cols]
print(movies.head(5))

# Viewing column statistics (numeric):

print(movies.describe().transpose())

# Viewing datatype of a column:

print(movies.dtypes)

# Number of times the datatype is present:

print(movies.dtypes.value_counts())


# Viewing datatype of a single column:

print(movies.profit.dtypes)
print(movies.title.dtypes)


# checking memory usage by column:

print(movies.memory_usage())













