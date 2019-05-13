#!/usr/bin/env python
# coding: utf-8

# In[62]:


import os
from bs4 import BeautifulSoup as bs
import urllib3
import requests
from splinter import Browser
import pandas as pd


# In[63]:


# browser=Browser('chrome')
def init_browser():
    executable_path = {'executable_path':'chromedriver'}
    return Browser('chrome',**executable_path,headless=False)

def scrape():
    browser = init_browser()
    marsd = {}


# NASA Mars News
# 

# In[34]:


# url1='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
# response1=requests.get(url1)
# soup1=bs(response1.content,'html.parser')
# result1=soup1.find('ul',class_='content_title')


# In[35]:


url1='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url1)
html=browser.html
soup=bs(html,'html.parser')


# In[36]:


title=soup.find(class_='content_title')
news_title=title.find('a').text
news_para=soup.find(class_='article_teaser_body').text


# Mars Space Images

# In[37]:


url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)
html=browser.html
soup=bs(html,'html.parser')


# In[38]:


button=soup.find(class_='button')
imgurl=button['data-link']


# In[39]:


urlh='https://www.jpl.nasa.gov'
featured_image_url=urlh+imgurl


# Mars Weather

# In[40]:


url3='https://twitter.com/marswxreport?lang=en'
browser.visit(url3)
html=browser.html
soup=bs(html,'html.parser')


# In[41]:


twit=soup.find(class_='js-tweet-text-container').text
twit=twit.strip()
mars_weather=twit[:-26]


# Mars Facts

# In[42]:


url4='https://space-facts.com/mars/'
browser.visit(url4)
html=browser.html
soup=bs(html,'html.parser')


# In[43]:


fact=pd.read_html(url4)
fact


# Mars Hemispheres
# 
# 

# In[64]:


url5='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)
html=browser.html
soup=bs(html,'html.parser')


# In[89]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[97]:


browser.find_link_by_partial_href('/search/map/Mars/Viking/').click()


# In[92]:


element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID('itemLink product-item'))))


# In[98]:


# I don't know what's happening but I have to move on.


# In[ ]:




