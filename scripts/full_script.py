from pyspark.sql import *

spark = SparkSession.builder.getOrCreate()

for year in range(2006, 2017):
    for month in range(1, 13):
        path = "hdfs:///datasets/reddit_data/{}/RC_{}-{num:02d}.bz2".format(year, year, num=month)
        data = spark.read.json(path)
        data = data.filter(data['subreddit'] == 'politics').filter(data['body'] != '[deleted]')
        data = data.select('author', 'body', 'created_utc', 'gilded', 'score', 'ups', 'downs', 'name')
        data.write.format('json').save('politics_{}_{}.json'.format(year, month))
