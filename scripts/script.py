from pyspark.sql import *

spark = SparkSession.builder.getOrCreate()

DATASET_PATH = "hdfs:///datasets/reddit_data"
PATH_2007 = DATASET_PATH + "/2007/RC_2007-12.bz2"

reddit = spark.read.json(PATH_2007)

reddit.printSchema()

reddit = reddit.filter(reddit["subreddit"] == "politics").filter(reddit['body'] != '[deleted]')
reddit = reddit.select('author', 'body', 'created_utc', 'gilded', 'score', 'ups', 'downs', 'name')

reddit.write.mode(SaveMode.Overwrite).format('json').save('sample_2007_12.json')
