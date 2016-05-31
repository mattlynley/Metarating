import requests
from bs4 import BeautifulSoup

def getarticles(url):

  r = requests.get(url)
  r_html = r.text

  soup = BeautifulSoup(r_html, "html.parser")
  title = soup.find(class_="story-heading").string

  return(title)

print(getarticles('http://www.nytimes.com/'))