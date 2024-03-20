# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:48:47 2024

@author: Keelan
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import random
import bisect
import collections

#store the url in a variable
url ='https://liquipedia.net/dota2/Tier_1_Tournaments'


#access the contents of the webpage
response = requests.get(url, headers = {'User-Agent': 'Chrome'})

#extract HTML from response
page_content = response.content

#parse HTML
soup = BeautifulSoup(page_content, 'lxml')

#find all tables in the HTML
my_tables = soup.find_all('div', attrs = {"class": "gridTable"})

print(my_tables)