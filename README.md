# IST3134 Group Assignment
## Project Structure
This project analyzes word frequency in review datasets using **two processing approaches**:
- Hadoop **MapReduce** (Python-based)
- **Apache Spark** (Java-based, non-MapReduce)

## Folder Structure
.
├── mapreduce/
│   ├── results/
│   │   ├── final_sorted/      <- Top 100 words sorted from highest to lowest frequency
│   │   └── wordcount/        <- Raw word count output from MapReduce
│   ├── byLowReview/
│   │   ├── mapper/
│   │   │   ├── mapper.py
│   │   │   └── reducer.py
│   │   └── data_cleaning.py
│   ├── byHighReview/
│   │   ├── mapper/
│   │   │   ├── mapper.py
│   │   │   └── reducer.py
│   │   └── data_cleaning.py
│   └── byCategory/
│       ├── mapper/
│       │   ├── mapper.py
│       │   └── reducer.py
│       └── category_cleaning.py
│       └── data_cleaning.py
│
└── nonmapreduce/
    ├── results/
    │   ├── final_sorted      <- Same as above, Spark-generated
    │   └── wordcount         <- Raw output from Spark jobs
    └── code/
        ├── WordCount.java
        ├── ByLowReview.java
        ├── ByHighReview.java
        └── ByCategory.java


This onedrive link contains the datasets used for the assignment:
https://imailsunwayedu-my.sharepoint.com/:f:/g/personal/19101153_imail_sunway_edu_my/EuMq0bkIpQJGnRaeWBjPS_4BvFYuaLY55x4p4G45XrmPpQ?e=P2OQv2
