#!/bin/bash
spark-submit --master yarn --deploy-mode client --driver-memory 4G --num-executors 5 --executor-memory 4G --executor-cores 5 $1
