from pyspark.sql import SparkSession
import re

# 1. Start Spark session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("WordCountByCategory") \
    .getOrCreate()

sc = spark.sparkContext
rdd = sc.textFile("hdfs:///user/hadoop/IST3134/nonMapReduce/dataset/Amazon_byCategory.txt")

# mapping words to category
def parse_and_tokenize(line):
    parts = line.strip().split("\t")
    if len(parts) != 3:
        return []

    rating, category, text = parts
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)
    return [((category, word), 1) for word in words]

word_pairs = rdd.flatMap(parse_and_tokenize)
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# reshaping the columns (category, word, count)
category_word_counts = word_counts.map(lambda x: (x[0][0], x[0][1], x[1]))

# group by category and sort by frequency
sorted_counts = (
    category_word_counts
    .map(lambda x: (x[0], (x[1], x[2])))  # (category, (word, count))
    .groupByKey()
    .flatMapValues(lambda wc: sorted(wc, key=lambda x: -x[1]))  # sort by count desc
    .map(lambda x: (x[0], x[1][0], x[1][1]))  # (category, word, count)
)

# save
sorted_counts.saveAsTextFile("hdfs:///user/hadoop/IST3134/nonMapReduce/output3")
sc.stop()
