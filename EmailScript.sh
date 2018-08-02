#! /bin/bash

#fetch attachments from webmail client
/usr/bin/python ~/EmailReader/EmailReader.py
DIR_TO_PUT_UNZIPPED_FILES="/home/systems/Renulogs"
if [ ! -d $DIR_TO_PUT_UNZIPPED_FILES ]; then
  mkdir -p $DIR_TO_PUT_UNZIPPED_FILES
fi

for file in ~/Attachments/*.zip;
 do
 unzip -qq "$file" -d ~/Renulogs;
# rm ~/Attachments/*;
 done
rm ~/Attachments/*;
#rm ~/verbose;

