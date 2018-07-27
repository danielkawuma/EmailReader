
import requests, os

from datetime import date

#file_name = 'renu_20180505.txt'
#retrieved_file_dir = '~/TextFiles'
#filename with date appended
file_name = "renu_" + str(date.today().strftime('%Y%m%d')) + ".txt"

#url to connect to website with username and password provided
file_url = 'https://renu:b2ef86e451d61912@www.cymru.com/renu/'+file_name+''

#fetching the text file  from the website
response = requests.get(file_url)

#passing the text file conttents to a variable `retrieved_file`
retrieved_file = response.content
print(retrieved_file)



