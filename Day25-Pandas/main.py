import pandas

squirrel = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

color = squirrel['Primary Fur Color'].value_counts()

print(color)
# color_DF = pandas.DataFrame(color)
# color_DF.to_csv('squirrel_count.csv')