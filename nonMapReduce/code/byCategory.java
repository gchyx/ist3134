import org.apache.spark.api.java.*;
import org.apache.spark.api.java.function.*;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;
import scala.Tuple3;

import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class ByCategory {
    public static void main(String[] args) {

        SparkSession spark = SparkSession.builder()
                .appName("WordCountByCategory")
                .master("local[*]")
                .getOrCreate();

        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());

        JavaRDD<String> rdd = sc.textFile("file:///home/hadoop/IST3134/nonMapReduce/dataset/category_reviews.txt");

        // flatMap to ((category, word), 1)
        JavaPairRDD<Tuple2<String, String>, Integer> wordPairs = rdd.flatMapToPair((PairFlatMapFunction<String, Tuple2<String, String>, Integer>) line -> {
            List<Tuple2<Tuple2<String, String>, Integer>> result = new ArrayList<>();
            String[] parts = line.trim().split("\t");
            if (parts.length != 3) return result.iterator();

            String rating = parts[0];
            String category = parts[1];
            String text = parts[2].toLowerCase();

            Pattern pattern = Pattern.compile("\\b\\w+\\b");
            Matcher matcher = pattern.matcher(text);
            while (matcher.find()) {
                String word = matcher.group();
                result.add(new Tuple2<>(new Tuple2<>(category, word), 1));
            }
            return result.iterator();
        });

        // count by (category, word)
        JavaPairRDD<Tuple2<String, String>, Integer> wordCounts = wordPairs.reduceByKey(Integer::sum);

        // map to (category, word, count)
        JavaRDD<Tuple3<String, String, Integer>> categoryWordCounts = wordCounts.map(
                tuple -> new Tuple3<>(tuple._1._1, tuple._1._2, tuple._2)
        );

        // group by category
        JavaPairRDD<String, Iterable<Tuple2<String, Integer>>> grouped = categoryWordCounts.mapToPair(
                tuple -> new Tuple2<>(tuple._1(), new Tuple2<>(tuple._2(), tuple._3()))
        ).groupByKey();

        // sort words by count descending and format output
        JavaRDD<String> sortedOutput = grouped.flatMap(tuple -> {
            String category = tuple._1;
            List<Tuple2<String, Integer>> wordList = new ArrayList<>();
            tuple._2.forEach(wordList::add);
            wordList.sort((a, b) -> b._2.compareTo(a._2)); // sort descending

            List<String> output = new ArrayList<>();
            for (Tuple2<String, Integer> word : wordList) {
                output.add(category + "\t" + word._1 + "\t" + word._2);
            }
            return output.iterator();
        });

        // save
        sortedOutput.saveAsTextFile("file:///home/hadoop/IST3134/nonMapReduce/output/output3");

        sc.stop();
        spark.stop();
    }
}
