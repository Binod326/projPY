#Author: Binod Maharjan
#Program Name: Name Game
#Date: 12/02/2023 
#Version: 1.0.0
#Version date: 12/02/2023

#we need to have two libraries to do web scrapping
#urllip2 is available by default and beautifulsoup4 library need to install by using pip install beautifulsoup4

# Install all the requirements first
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traveesal
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment
title = soup.title
print(title)