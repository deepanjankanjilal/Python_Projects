# Reading CSV file using pandas library
import pandas
df = pandas.read_csv('C:\Python3\hrdata.csv')
print(df)

df = pandas.read_csv('C:\Python3\hrdata.csv', index_col='Name')
print(df)

df = pandas.read_csv('C:\Python3\hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)

df = pandas.read_csv('C:\Python3\hrdata.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)
