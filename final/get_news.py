import requests
import json 
import itertools
#from fuzzywuzzy import fuzz


#Getting 
def api_call(tag):
       url = (f'http://newsapi.org/v2/top-headlines?'
       'sources=%s&'
       'apiKey=ce14cd708c98400dae8398e4ffae83c6'%tag)
       response = requests.get(url)
       #Unformatted JSON response 
       json_string = response.json()
       #Converting unformatted JSON response into a string
       data_temp = json.dumps(json_string)
       #Converting string into formatted JSON
       data = json.loads(data_temp)
       return data

#main function
def get_data():
       #news sources 
       br = 'bleacher-report'
       espn = 'espn'
       bbc = 'bbc-sport'

       #retrieving data from chosen news sources
       br_rawdata = api_call(br)
       espn_rawdata = api_call(espn)
       bbc_rawdata = api_call(bbc)

       #pulling article information from JSON data
       br_articles = br_rawdata['articles']
       espn_articles = espn_rawdata['articles']
       bbc_articles = bbc_rawdata['articles']
       
       #creating a master list
       master_list = espn_articles + br_articles  + bbc_articles
       #print(master_list)
       #print (fuzz.token_set_ratio(master_list[4]['description'],master_list[0]['description']))
       #for i in range(len(master_list)):
              #print ('Title: ' + str(master_list[i]['title']))
              #print ('Author:' + str(master_list[i]['author']))
              #print ('Summary: ' + str(master_list[i]['description']))
              #print ('Link: ' + str(master_list[i]['url']))
       return master_list
            
              

