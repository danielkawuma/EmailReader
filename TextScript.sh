#! /bin/bash

DIR_TO_PUT_TEXT_FILES="/home/systems/Renulogs"
if [ ! -d $DIR_TO_PUT_TEXT_FILES ]; then
  mkdir -p $DIR_TO_PUT_TEXT_FILES
fi


 wget -qq --http-user=renu --http-password=b2ef86e451d61912 https://www.cymru.com/renu/renu_`date -d "yesterday" +%Y%m%d`.txt -P ~/Renulogs/
