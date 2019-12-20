# this will be a command that lets us validate a model in our looker environment

import csv #to write to csvs
import yaml #to read config file
import requests #to connect to looker api
from pprint import pprint
from lookerapi import LookerApi


### ------- HERE ARE PARAMETERS TO CONFIGURE -------

host = 'looker'
output_csv_name = 'output.csv'

### ------- OPEN CONFIG FILE AND INSTANTIATE API -------

with open('config.yml', 'r') as myfile:
    params = yaml.safe_load(myfile)
    my_host = params['hosts'][host]['host']
    my_secret = params['hosts'][host]['secret']
    my_token = params['hosts'][host]['token']
    
looker_api = LookerApi(my_token, my_secret, my_host)

### ------- GET AND PRINT THE LOOK -------

space_data = looker.get_all_spaces(fields='id, parent_id, name')

data = looker.get_content_validation()


host_url = my_host[:my_host.index(":19999")]
broken_content = data['content_with_errors']
# pprint(broken_content)
