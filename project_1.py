#scrape all urls of website using python

from bs4 import  BeautifulSoup
import requests
#creating empty list
urls=[]
#function created
def screape(site):
    #getting the request from url
    r=requests.get(site).text
    #print(r)
    #converting the text
    soup=BeautifulSoup(r,'html.parser')
    for i in soup.find_all("a"):
        link=i.attrs['href']
        if link.startswith('/'):
            site=site+link
            print(site,'\n')


'''
          site=site+link
          if site not in urls:
              urls.append(site)'''


if __name__=='__main__':
    #website to be scrape

    screape('https://www.programiz.com/')