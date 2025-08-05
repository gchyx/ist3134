# IST3134 Group Assignment
## Project Structure
This project analyzes word frequency in review datasets using **two processing approaches**:
- Hadoop **MapReduce** (Python-based)
- **Apache Spark** (Java-based, non-MapReduce)

## Folder Structure
### 1. MapReduce Section
The MapReduce implementation is organized into multiple folders based on different analysis categories. These are:

- **byLowReview**
- **byHighReview**
- **byCategory**

Each of these category folders contains the following:
A "**_mapper_**" folder, which includes the Python scripts for the Mapper and Reducer processes.
A **_data cleaning Python script_**, which is placed outside the "mapper" folder. This script is used to clean and prepare the data before running the MapReduce job.
In addition to these categories, there is also a "**_results_**" folder. The results folder includes:
"**_finalSorted_**" folder, which contains the top 100 most frequently used words .txt files, sorted from highest to lowest frequency.
"**_wordcount_**" folder, which includes the raw word count outputs from the MapReduce process before any sorting is applied.

### 2. Non-MapReduce Section
This section contains two folders:

"**_code_**" folder, which includes Java scripts written for Apache Spark. These scripts are responsible for processing the dataset using Spark's core features without the traditional MapReduce structure.

"**_results_**" folder, which contains the output similar to the MapReduce section:
- A folder with the top 100 sorted words by frequency files.
- A word count folder with files containing raw counts of all the words found in the dataset.

This onedrive link contains the datasets used for the assignment:
https://imailsunwayedu-my.sharepoint.com/:f:/g/personal/19101153_imail_sunway_edu_my/EuMq0bkIpQJGnRaeWBjPS_4BvFYuaLY55x4p4G45XrmPpQ?e=P2OQv2
