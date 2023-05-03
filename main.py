# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
Final project
Yurii Parzhyn
"""
from datetime import datetime

from pyspark import SparkConf
from pyspark.sql import SparkSession

# from task1 import task1
# from task2 import task2
# from task3 import task3
# from task4 import task4
# from task5 import task5
from task6 import task6
from task7 import task7
from task8 import task8


def main():
    start_time = datetime.now()
    spark_session = (SparkSession.builder
                     .master('local')
                     .appName('imdb spark prob')
                     .config(conf=SparkConf())
                     .getOrCreate())
    # Task 1:
    # imdb_df = read_spark_df(spark_session, sts.TITLE_AKAS_PATH, sts.title_akas_schema)
    # imdb_df.show()
    # imdb_df.printSchema()
    # task1(df=imdb_df, write_in_file=False)

    # Task 2:
    # imdb_df = read_spark_df(spark_session, sts.NAME_BASICS_PATH, sts.name_basics_schema)
    # imdb_df.show()
    # imdb_df.printSchema()
    # task2(df=imdb_df, write_in_file=False)

    # Task 3:
    # imdb_df = read_spark_df(spark_session, sts.TITLE_BASICS_PATH, sts.title_basics_schema)
    # imdb_df.show()
    # imdb_df.printSchema()
    # task3(df=imdb_df, write_in_file=True)

    # Task 4:
    # task4(spark_session, write_in_file=False)

    # Task 5:
    # task5(spark_session, write_in_file=True)

    # Task 6:
    # task6(spark_session, write_in_file=False)

    # Task 7:
    # task7(spark_session, write_in_file=True)

    # Task 8:
    task8(spark_session, write_in_file=True)

    print('All operations completed in:', datetime.now() - start_time)


if __name__ == "__main__":
    main()

