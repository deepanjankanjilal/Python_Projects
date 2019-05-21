# Creating a dataframe using List: DataFrame can be created using a single list or a list of lists.

# import pandas as pd
# importing numpy as np
import pandas as pd
import numpy as np

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print("Creating dataframe from list using pandas" + df)

# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.

# initialise data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)

# Import pandas package and selecting specific columns

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])

# importing pandas package and selecting specific rows

# making data frame from csv file
data = pd.read_csv("C:\Python3\player.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)

# importing pandas package and selecting a single column

# making data frame from csv file
data = pd.read_csv("C:\Python3\player.csv", index_col="Name")

# retrieving columns by indexing operator
first = data["Age"]
print(first)

# Selecting single row using iloc method

# making data frame from csv file
data = pd.read_csv("C:\Python3\player.csv", index_col="Name")

# retrieving rows by iloc method
row2 = data.iloc[3]

print(row2)

# Checking for missing values using isnull() and notnull() :

# dictionary of lists
dct = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dct)

# using isnull() function
df.isnull()

# Filling missing values using fillna(), replace() and interpolate() :

# dictionary of lists
dct = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from dictionary
df = pd.DataFrame(dct)

# filling missing value using fillna()
df.fillna(0)

# Dropping missing values using dropna() :

# dictionary of lists
dct = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}

# creating a dataframe from dictionary
df = pd.DataFrame(dct)
print(df)

# using dropna() function
df.dropna()

# Iterating over rows :
# dictionary of lists
dct = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dct)

print(df)
# iterating over rows using iterrows() function
for i, j in df.iterrows():
    print(i, j)
    print()

# Iterating over Columns :

# dictionary of lists
dct = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dct)
print(df)

# creating a list of dataframe columns
columns = list(df)
for i in columns:
    # printing the third element of the column
    print(df[i][2])
