# Spark 2 - Text File
# -------------------------------------------------------------------------------------------------------------------------------------
# En este script se lee el contenido de un archivo txt y se convierte en un RDD.
# Un archivo se interpreta como una lista, en la que cada elemento corresponde a una linea del archivo.

from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[1]').appName('ReadingAFile').getOrCreate()

file = spark.sparkContext.textFile('documents/lorem ipsum.txt')

print(f'No. lines: {len(file.collect())}')
print(file.collect()[0])

print("Finished")