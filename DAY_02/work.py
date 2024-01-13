from pandas import DataFrame, read_csv, Series

datafile='../DATA/movies.csv'
movieDF=read_csv(datafile)

print("hello")

#3번 
# print(movieDF.columns)

item = Series()
Column_data=[item*len(movieDF.columns)]
for idx, column in enumerate(movieDF.columns) :
    print(idx, column)
    Column_data[idx]=movieDF.loc[column]
    print(Column_data[idx])