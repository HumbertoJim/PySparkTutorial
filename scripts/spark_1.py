# Spark 1 - RDD
# -------------------------------------------------------------------------------------------------------------------------------------
# En este script se muestra como crear una session de spark. Asi, se crea una lista de python y se convierte en un RDD.

# import spark session
from pyspark.sql import SparkSession

# create or get the session
spark = SparkSession.builder.master('local[1]').appName('FirstExample').getOrCreate()

# representation of python data
data = [
    ('Java', 20000),
    ('Python', 100000),
    ('R', 5000),
    ('Scala', 3000)
]

# convert python list to a rdd
rdd = spark.sparkContext.parallelize(data)
print(rdd.collect())

print("Finished")