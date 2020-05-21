#!/bin/bash

#
# @Purpose
#	download answer for "Think Python" book easily
#
# @Usage
#    bash dl_answer.sh answer_file
#    -answer_file: answer file name 
#

DOWNLOAD_LINK="http://thinkpython2.com/code/"
ANSWER_FILE=$1

wget ${DOWNLOAD_LINK}${ANSWER_FILE}
