from pyspark.sql import *

spark = SparkSession.builder.getOrCreate()

DATASET_PATH = "hdfs:///datasets/reddit_data"
PATH_2008 = DATASET_PATH + "/2008/RC_2008-10.bz2"
PATH_2012 = DATASET_PATH + "/2012/RC_2012-10.bz2"
PATH_2016 = DATASET_PATH + "/2016/RC_2016-10.bz2"

reddit_2008 = spark.read.json(PATH_2008)
reddit_2012 = spark.read.json(PATH_2012)
reddit_2016 = spark.read.json(PATH_2016)

reddit_2008 = reddit_2008.filter(reddit_2008["subreddit"] == "politics").filter(reddit_2008['body'] != '[deleted]')
reddit_2008 = reddit_2008.select('author', 'body', 'created_utc', 'gilded', 'score')
reddit_2008.write.format('json').save('sample_2008_10.json')

reddit_2012 = reddit_2012.filter(reddit_2012["subreddit"] == "politics").filter(reddit_2012['body'] != '[deleted]')
reddit_2012 = reddit_2012.select('author', 'body', 'created_utc', 'gilded', 'score')
reddit_2012.write.format('json').save('sample_2012_10.json')

reddit_2016 = reddit_2016.filter(reddit_2016["subreddit"] == "politics").filter(reddit_2016['body'] != '[deleted]')
reddit_2016 = reddit_2016.select('author', 'body', 'created_utc', 'gilded', 'score')
reddit_2016.write.format('json').save('sample_2016_10.json')
