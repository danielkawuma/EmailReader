#! /bin/bash

#fetch attachments from webmail client
/usr/bin/python ~/logReaders/EmailReader.py

for file in ~/Attachments/*.zip;
 do
 unzip -qq "$file" -d ~/Renulogs;
# rm ~/Attachments/*;
 done
rm ~/Attachments/*;
#rm ~/verbose;

