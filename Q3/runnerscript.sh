#!/usr/bin/bash
STREAM_JAR=$1
LOCAL_INP=$2
HDFS_INP=$3
HDFS_OUT=$4
FILES=$5

# put files on hdfs
cat "${LOCAL_INPUT}" | ./preprocess.py | hdfs dfs -put - "${HDFS_INPUT_DIR}/input.txt"


hdfs dfs -rm -r ${HDFS_INP}example_input ${HDFS_OUT}example_output/
hdfs dfs -mkdir -p ${HDFS_INP}example_input/
hdfs dfs -put ${LOCAL_INP} ${HDFS_INP}example_input/

hadoop jar $STREAM_JAR \
-D mapred.reduce.tasks=3 \
-input ${HDFS_INP}example_input/ \
-output $HDFS_OUT/example_output/ \
-mapper ${FILES}mapper.py \
-file ${FILES}mapper.py \
-reducer ${FILES}reducer.py \
-file ${FILES}reducer.py




