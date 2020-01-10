import os

from pyspark.sql import Window
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

os.environ['HADOOP_HOME'] = "C:\\Users\\esscay\\hadoop-winutils-2.6.0"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

df = spark.read.format('csv') \
    .options(header='true', inferSchema='true') \
    .load('C:/Users/esscay/PycharmProjects/pyspark-demo/com/daniel/input-files/emp.csv')
df.createGlobalTempView("emp")

df = spark.sql("select * from global_temp.emp");
# df1 = df1.filter(df1.age > 30)
print("Raw Output")
df.show()

df1 = df.select(df.name, df.age, F.when(df.age > 30, 0).otherwise(1).alias("cond_flag"))
window = Window.partitionBy("name").orderBy("age").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df1 = df1.withColumn("rank", F.rank().over(window)) \
    .withColumn("min", F.min('age')
                .over(window))

print(f'In Spark API')
df1.show()

df2 = df.selectExpr("*", "case when age > 30 then 0 else 1 end as cond_flag",
                    "rank() over(partition by name order by age) as rank",
                    "min(age) over(partition by name order by age) as min")

print(f'In Spark SQL')
df2.show()
