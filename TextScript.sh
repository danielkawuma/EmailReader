#! /bin/bash

DIR_TO_PUT_TEXT_FILES="/home/daniel/Renulogs"
if [ ! -d $DIR_TO_PUT_TEXT_FILES ]; then
  mkdir -p $DIR_TO_PUT_TEXT_FILES
fi


 /usr/bin/python3 /home/daniel/EmailReader/TextFileExtractor.py > /home/daniel/Renulogs/renu_`date +%Y%m%d`.txt 2>>/home/daniel/Renulogs/error.log
