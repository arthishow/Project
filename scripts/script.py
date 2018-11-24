from pyspark.sql import *

spark = SparkSession.builder.getOrCreate()

DATASET_PATH = "hdfs:///datasets/reddit_data"
PATH_2007 = DATASET_PATH + "/2007/RC_2007-12.bz2"

print(PATH_2007)
reddit = spark.read.json(PATH_2007) # open the file
reddit.show(5)
reddit.printSchema()
