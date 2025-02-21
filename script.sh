#!/bin/bash
# Script to split Qualys compliance reports
###########################################################################
# PARAMETER : 
#  1 - File to split (should be in CSV)
#
#
###########################################################################
# CHANGELOG : 
###########################################################################
#   DATE		AUTHOR			REVISION
# 21/02/2025	J. Blion		Creation
#
#
###########################################################################

SUMMARY_TAG="^Host Statistics (Percentage of Controls Passed per Host)$"
ASSETS_TAG="^ASSET TAG$"
RESULTS_TAG="^\"RESULTS\"$"

usage() 
{
	echo "Usage: $0 fiile_to_split"
	exit 99
}


if [ $# -ne 1 ]
then
		usage
fi

SOURCE_FILE=$1
DEST_SUMMARY_FILE="summary"
DEST_ASSETS_FILE="assets"
DEST_RESULTS_FILE="results"

#SUFFIX="$(uuid -F SIV).csv"
SUFFIX=".csv"

LINES_COUNT=$(wc -l $SOURCE_FILE | awk '{print $1}')
START_OF_SUMMARY=$(egrep -hn "$SUMMARY_TAG" $SOURCE_FILE  | awk -F":" '{print $1}')
START_OF_ASSETS=$(egrep -hn "$ASSETS_TAG" $SOURCE_FILE  | awk -F":" '{print $1}')
START_OF_RESULTS=$(egrep -hn "$RESULTS_TAG" $SOURCE_FILE  | awk -F":" '{print $1}')

SIZE_OF_SUMMARY=$(($START_OF_ASSETS - $START_OF_SUMMARY -1))
SIZE_OF_ASSETS=$(($START_OF_RESULTS - $START_OF_ASSETS -1))
SIZE_OF_RESULTS=$(($LINES_COUNT - $START_OF_RESULTS))

head -n $(($START_OF_ASSETS - 1)) $SOURCE_FILE | tail -n $SIZE_OF_SUMMARY > $DEST_SUMMARY_FILE.$SUFFIX
head -n $(($START_OF_RESULTS - 1)) $SOURCE_FILE | tail -n $SIZE_OF_ASSETS > $DEST_ASSETS_FILE.$SUFFIX
tail -n $SIZE_OF_RESULTS $SOURCE_FILE > $DEST_RESULTS_FILE.$SUFFIX
