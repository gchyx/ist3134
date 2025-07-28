from pyspark.sql import SparkSession
import re

# start spark session
spark = SparkSession.builder\
  .master("local[*]")\
  .appName("WordCount")\
  .getOrCreate()

sc = spark.sparkContext  
amazon_rdd = sc.textFile("hdfs:///user/hadoop/IST3134/nonMapReduce/data/category_reviews.txt")

# filter ratings to <= 2 stars
def lowRating(line):
    parts = line.strip().split()
    if not parts:
        return False
    try:
        return float(parts[0]) <= 2.0
    except:
        return False

filtered_rdd = amazon_rdd.filter(lowRating)

# clean review text: remove punctuation, lowercase
def clean_text(line):
    parts = line.strip().split("\t")
    if len(parts) != 2:
        return []

    review = parts[1].lower()
    words = re.findall(r"\b\w+\b", review)
    return words

cleaned_rdd = filtered_rdd.flatMap(clean_text)

# word Count
word_counts = (
    cleaned_rdd
    .flatMap(lambda line: line.split())
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

# save
word_counts.saveAsTextFile("hdfs:///user/hadoop/IST3134/nonMapReduce/output1.txt")
sc.stop()
