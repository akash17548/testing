import pyspark

from pyspark.sql import SparkSession
import pandas as pd

spark =SparkSession.builder.appName("testing").getOrCreate()

df =spark.read.csv("C:\\Users\\akash\\OneDrive\\Desktop\\vscodepythondemo\\data_set\\pyspark_test.csv",header=True,inferSchema=True)

df.show()

