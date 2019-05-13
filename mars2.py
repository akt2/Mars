from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {'executable_path':'chromedriver'}
    return Browser('chrome',**executable_path,headless=False)

def scrape():
    browser = init_browser()

    url1='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url1)
    html=browser.html
    soup=bs(html,'html.parser')

    title=soup.find(class_='content_title')
    news_title=title.find('a').text
    news_para=soup.find(class_='article_teaser_body').text

    url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html=browser.html
    soup=bs(html,'html.parser')

    button=soup.find(class_='button')
    imgurl=button['data-link']

    urlh='https://www.jpl.nasa.gov'
    featured_image_url=urlh+imgurl

    url3='https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html=browser.html
    soup=bs(html,'html.parser')

    twit=soup.find(class_='js-tweet-text-container').text
    twit=twit.strip()
    mars_weather=twit[:-26]

    url4='https://space-facts.com/mars/'
    browser.visit(url4)
    html=browser.html
    soup=bs(html,'html.parser')

    fact=pd.read_html(url4)

    # url5='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(url5)
    # html=browser.html
    # soup=bs(html,'html.parser')

    mars={
        'news_paragraph': news_para,
        'featured_image-url': featured_image_url,
        'mars_weather': mars_weather,
        'fact_table': fact
    }

    browser.quit()

    return mars