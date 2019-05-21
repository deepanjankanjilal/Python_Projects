# Writing data into CSV using pandas library
import pandas
df = pandas.read_csv('C:\Python3\hrdata.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('C:\Python3\hrdata_modified.csv')