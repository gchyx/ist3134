import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;

import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.apache.spark.api.java.function.FlatMapFunction;

public class byHighRating {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("WordCount")
                .master("local[*]")
                .getOrCreate();

        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());
        JavaRDD<String> amazonRdd = sc.textFile("file:///home/hadoop/IST3134/nonMapReduce/dataset/Amazon_Fashion.txt");

        // filter with rating == 5.0
        JavaRDD<String> filteredRdd = amazonRdd.filter(line -> {
            String[] parts = line.trim().split("\\s+", 2);
            if (parts.length < 1) return false;
            try {
                return Double.parseDouble(parts[0]) == 5.0;
            } catch (NumberFormatException e) {
                return false;
            }
        });

        // clean text and extract words
        JavaRDD<String> cleanedWords = filteredRdd.flatMap(
            (FlatMapFunction<String, String>) line -> {
                String[] parts = line.trim().split("\t", 2);
                if (parts.length != 2) return java.util.Collections.emptyIterator();

                String review = parts[1].toLowerCase();
                Pattern wordPattern = Pattern.compile("\\b\\w+\\b");
                Matcher matcher = wordPattern.matcher(review);

                List<String> words = new java.util.ArrayList<>();
                while (matcher.find()) {
                    words.add(matcher.group());
                }
                return words.iterator();
            }
        );
        // word count
        JavaPairRDD<String, Integer> wordCounts = cleanedWords
                .mapToPair(word -> new Tuple2<>(word, 1))
                .reduceByKey(Integer::sum);

        // save
        wordCounts.saveAsTextFile("file:///home/hadoop/IST3134/nonMapReduce/output/output2");
        sc.stop();
    }
}