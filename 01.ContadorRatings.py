from pyspark import SparkContext, SparkConf
import collections

conf = SparkConf().setMaster('local').setAppname('ContadorRatings')
sc = SparkContext(conf=conf)

lines = sc.TextFile('C:/Users/jmart/Documents/Platzi/Data Science/Apache Spark/Datasets/ml-100k/u.data')
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))

for key, value in sortedResults:
    print(f'{key}, {value}')