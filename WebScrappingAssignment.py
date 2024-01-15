#!/usr/bin/env python
# coding: utf-8

# 1)

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[ ]:


page=requests.get("https://en.wikipedia.org/wiki/Main_Page")

soup = BeautifulSoup(page.content)

header_tags =['h1','h2','h3','h4','h5','h6']

for tags in soup.find_all(header_tags):
    print(tags.name,'-',tags.text)


# 2)

# In[ ]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')

soup = BeautifulSoup(page.content)

p_names = []
for i in soup.find_all('div',class_="presidentListing"):
    p_names.append(i.find("h3").text.split("(")[0])
    
term = []
for i in soup.find_all('div',class_="presidentListing"): 
    term.append(i.find("p").text.split("(")[0])

df = pd.DataFrame({"President Name":p_names,"Term of Office":term})
df


# 3)

# a)

# In[ ]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")

soup = BeautifulSoup(page.content)

team= []
for i in soup.find_all('span',class_="u-hide-phablet"):
    team.append(i.text)

matches=[]
for i in list(soup.find_all('td',attrs={'table-body__cell u-center-text'}))[::2]:
    matches.append(i.text)
    
points= []
for i in list(soup.find_all('td',attrs={'table-body__cell u-center-text'}))[1::2]:
    points.append(i.text)
    
rating=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
df = pd.DataFrame({"Team":team[:10],"Matches":matches[:10] ,"Points":points[:10] ,"Rating":rating[:10]})
df


# b)

# In[ ]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")

soup = BeautifulSoup(page.content)

name = []
for i in soup.find('div',class_="rankings-block__banner--name"):
    name.append(i.text)                 
for i in soup.find_all('td',attrs="table-body__cell name")[:9]:
    name.append(i.text.split("\n")[1])
    
team = []
team1 = (soup.find('div',attrs={"rankings-block__banner--nationality"}).text)
team.append((team1[2:5]).replace('\n',''))
for i in soup.find_all('span',class_="table-body__logo-text")[:9]:
    team.append(i.text.replace('\n',''))
    
rating = []
rating.append((soup.find('div',attrs="rankings-block__banner--rating")).text)
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[:9]:
    rating.append(i.text)
    
print(len(name),len(team),len(rating))

df = pd.DataFrame({"Name of Batsmen":name,"Team":team,"Rating":rating})
df


# c)

# In[ ]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")

soup = BeautifulSoup(page.content)

name = []
for i in soup.find_all('div',class_="rankings-block__banner--name")[1:2]:
    name.append(i.text)
for i in soup.find_all('td',class_="table-body__cell name")[9:18]:
    name.append(i.text.replace('\n',''))
    
team = []
for i in soup.find_all('div',class_="rankings-block__banner--nationality")[1:2]:
    team.append(i.text.replace("\n","").split()[0])
for i in soup.find_all('span',class_="table-body__logo-text")[9:18]:
    team.append(i.text.replace('\n',''))
    
rating = []
for i in soup.find_all('div',class_="rankings-block__banner--nationality")[1:2]:
    rating.append(i.text.replace("\n","").split()[1])
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[9:18]:
    rating.append(i.text)
    
print(len(name),len(team),len(rating))

rank = range(1,11)

df = pd.DataFrame({"Name of baller":name,"Team":team,"ratings":rating},index=rank)
df


# 4)

# a)

# In[ ]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')

soup = BeautifulSoup(page.content)

rank = range(1,11)

team =[]
for i in soup.find_all('span',class_="u-hide-phablet")[:10]:
    team.append(i.text)
    
match =[]
for i in soup.find_all('td',class_="rankings-block__banner--matches"):
    match.append(i.text)
for i in soup.find_all('td',class_="table-body__cell u-center-text")[:18:2]:
    match.append(i.text)
    
point = []
for i in soup.find_all('td',class_="rankings-block__banner--points"):
    point.append(i.text)
for i in soup.find_all('td',class_="table-body__cell u-center-text")[1:19:2]:
    point.append(i.text)
    
rating = []
for i in soup.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    rating.append(i.text.replace("\n","").replace(" ",""))
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[:9]:
    rating.append(i.text)
    
print(len(team),len(point),len(match),len(rating))

df = pd.DataFrame({"Team":team,"Matches":match,"Points":point,"Rating":rating},index=rank)
df


# b)

# In[ ]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')

soup = BeautifulSoup(page.content)

Rank = range(1,11)

name = []
for i in soup.find('div',class_="rankings-block__banner--name"):
    name.append(i)
for i in soup.find_all('td',class_="table-body__cell name")[:9]:
    name.append(i.text.replace("\n",""))

team = []
team1 = (soup.find('div',attrs={"rankings-block__banner--nationality"}).text)
team.append((team1[2:5]).replace('\n',''))   
for i in soup.find_all('span',class_="table-body__logo-text")[:9]:
    team.append(i.text.replace('\n',''))

rating = []
rating.append((soup.find('div',attrs="rankings-block__banner--rating")).text)
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[:9]:
    rating.append(i.text)

print(len(name),len(team),len(rating))

df = pd.DataFrame({"Name of Player":name,"Team":team,"Rating":rating}, index = Rank)
df


# c)

# In[ ]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')

soup = BeautifulSoup(page.content)

Rank = range(1,11)

name = []

for i in soup.find_all('div',class_="rankings-block__banner--name")[2:]:
    name.append(i.text)
for i in soup.find_all('td',class_="table-body__cell name")[18:27]:
    name.append(i.text.replace("\n",""))

team = []

for i in soup.find_all('div',attrs="rankings-block__banner--nationality")[2:]:
    team.append(i.text.replace("\n","").replace(" ","")[:2])
for i in soup.find_all('span',class_="table-body__logo-text")[18:27]:
    team.append(i.text.replace('\n',''))

rating = []

for i in soup.find_all('div',attrs="rankings-block__banner--rating")[2:]:
    rating.append(i.text)
for i in soup.find_all('td',class_="table-body__cell u-text-right rating")[18:27]:
    rating.append(i.text)

print(len(name),len(team),len(rating))

df = pd.DataFrame({"Name of Player":name,"Team":team,"Rating":rating}, index = Rank)
df


# 5)

# In[ ]:


page=requests.get("https://www.cnbc.com/world/?region=world")

soup = BeautifulSoup(page.content)

headline = []
for i in soup.find_all('a',class_="LatestNews-headline"):
    headline.append(i.text)
    
time = []
for i in soup.find_all('time',class_="LatestNews-timestamp"):
    time.append(i.text)
    
url = []
for i in soup.find_all("a",class_="LatestNews-headline"):

    url.append(i.get("href"))
    
df = pd.DataFrame({"HEADLINE":headline, "TIME":time,"URL":url})
df


# 6)

# In[ ]:


page=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")

soup = BeautifulSoup(page.content)

p_title = []
for i in soup.find_all('a',class_="sc-5smygv-0 nrDZj"):
    p_title.append(i.text)
    
Authors = []
for i in soup.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    Authors.append(i.text)
    
Published_Date = []
for i in soup.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    Published_Date.append(i.text)

url = []
for i in soup.find_all("a",class_="sc-5smygv-0 nrDZj"):

    url.append(i.get("href"))

df = pd.DataFrame({"Paper Title":p_title, "Author":Authors,"Published Date":Published_Date, "URL":url})
df 


# 7)

# In[ ]:


page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")

soup = BeautifulSoup(page.content)

titles = []
for i in soup.find_all('div',class_="restnt-info cursor"):
    titles.append(i.text)

cuisine = []
for i in soup.find_all('div',class_="detail-info"):
    cuisine.append(i.text.split('|')[1])

Location = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)

rating = []
for i in soup.find_all('div',class_="rating-txt hide"):
    rating.append(i.text)

url = []
for i in soup.find_all('img',class_="no-img"):
    url.append(i['data-src'])

df = pd.DataFrame({"Restaurant name":titles, "Cuisine":cuisine, "Location":Location, "Ratings":rating, "URL":url})
df

