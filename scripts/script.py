from pyspark.sql import *

spark = SparkSession.builder.getOrCreate()

DATASET_PATH = "hdfs:///datasets/reddit_data"
PATH_2005 = DATASET_PATH + "/2005/RC_2005-12.bz2"

print(PATH_2005)
reddit = spark.read.json(PATH_2005) # open the file

reddit.printSchema()

reddit.write.format('json').save('/Users/arthishow/Desktop/reddit.json')
