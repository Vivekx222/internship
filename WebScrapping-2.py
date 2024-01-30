#!/usr/bin/env python
# coding: utf-8

# Q1

# In[ ]:


#Importing all the required libraries
from selenium import webdriver
import pandas as pd


# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


#webpage
driver.get('https://www.shine.com/')


# In[ ]:


#finding element for job search
job_title = driver.find_element_by_id('id_q')
job_title.send_keys('Data Analyst')


# In[ ]:


#finding element for job location
location = driver.find_element_by_id('id_l')
location.send_keys('Bangalore')


# In[ ]:


search_button = driver.find_element_by_xpath('//button[@type="submit"]')
search_button.click()


# In[ ]:


job_titles = driver.find_elements_by_xpath('//a[@class="job_title_anchor"]')
job_locations = driver.find_elements_by_xpath('//li[@class="w-30 mr-10 result-display-location"]/span')
company_names = driver.find_elements_by_xpath('//a[@class="result-display-company-name"]')
experience_required = driver.find_elements_by_xpath('//li[@class="w-30 mr-10 result-display-exp"]/span')

# extracting text of the job title
data = []
for i in range(10):
  job = {
  'Job Title': job_titles[i].text,
  'Job Location': job_locations[i].text,
  'Company Name': company_names[i].text,
  'Experience Required': experience_required[i].text
  }
  data.append(job)


# In[ ]:


#creating dataframe of the scraped data
df = pd.DataFrame(data)


# In[ ]:


driver.quit()


# Q2

# In[ ]:


imports requests
from bs4 import BeautifulSoup


# In[ ]:


#webpage
url = "https://www.shine.com"
response = requests.get(url)


# In[ ]:


#Entring search criteria and search button
job_title = "Data Scientist"
location = "Bangalore"
payload = {
  "search_query": job_title,
  "loc_query": location
}
response = requests.post(url, data=payload)


# In[ ]:


#Scrapeing the data for the first 10 jobs
soup = BeautifulSoup(response.content, "html.parser")
job_results = soup.find_all("div", class_="result-display")
job_data = []
for result in job_results[:10]:
  title = result.find("h2").text.strip()
  company = result.find("span", class_="company-name").text.strip()
  location = result.find("span", class_="location").text.strip()
  job_data.append({"Job Title": title, "Company Name": company, "Location": location})


# In[ ]:


#creating a dataframe of the scraped data
df = pd.DataFrame(job_data)


# In[ ]:


#Printing the dataframe
print(df)


# Q3

# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


#webpage
driver.get('https://www.shine.com/')


# In[ ]:


#Search query and click search button
search_box = driver.find_element_by_id('id_q')
search_box.send_keys('Data Scientist')

search_button = driver.find_element_by_id('id_l')
search_button.click()


# In[ ]:


#location and salary filters
location_filter = driver.find_element_by_xpath("//input[@value='Delhi/NCR']")
location_filter.click()

salary_filter = driver.find_element_by_xpath("//input[@value='3-6']")
salary_filter.click()


# In[ ]:


#Scrape the data for the first 10 jobs results
job_titles = driver.find_elements_by_xpath("//a[@class='job_title']")
job_locations = driver.find_elements_by_xpath("//li[@class='w-30 mr-10 result-display-location']")
company_names = driver.find_elements_by_xpath("//a[@class='result-display-company']")
experience_required = driver.find_elements_by_xpath("//li[@class='w-30 mr-10 result-display-exp']")


# In[ ]:


#Creating the dataframe od the scraped data
data = {'Job Title': [title.text for title in job_titles[:10]],
  'Job Location': [location.text for location in job_locations[:10]],
  'Company Name': [company.text for company in company_names[:10]],
  'Experience Required': [experience.text for experience in experience_required[:10]]}

df = pd.DataFrame(data)


# In[ ]:


driver.quit()


# Q4

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


#webpage
driver.get("http://www.flipkart.com/")


# In[ ]:


#Search for the sunglasses
search_box = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
search_box.send_keys('sunglasses')
search_box.submit()


# In[ ]:


#scrape the required attributes for the first 100 listings
sunglasses = driver.find_elements(By.XPATH, "//div[@class='_2kHMtA']")
data = []

for i in range(100):
  brand = sunglasses[i].find_element(By.XPATH, ".//div[@class='_2WkVRV']")
  description = sunglasses[i].find_element(By.XPATH, ".//a[@class='IRpwTa']")
  price = sunglasses[i].find_element(By.XPATH, ".//div[@class='_30jeq3 _1_WHN1']")
  
  data.append({
  'Brand': brand.text,
  'ProductDescription': description.text,
  'Price': price.text
  })


# In[ ]:


#Print the scraped data
for item in data:
  print(item)


# In[ ]:


driver.quit()


# Q5

# In[ ]:


#Send a GET request to the URL and parse the HTML content
url = "https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# In[ ]:


#find container that holds the reviews
reviews = soup.find_all('div', {'class': '_27M-vq'})


# In[ ]:


#Loop through the reviews and extract the required attributes:
for review in reviews[:100]:
  rating = review.find('div', {'class': '_3LWZlK _1BLPMq'}).text
  summary = review.find('p', {'class': '_2-N8zT'}).text
  full_review = review.find('div', {'class': 't-ZTKy'}).text


# In[ ]:


Q6


# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url="https://www.flipkart.com/"
driver.get(url)


# In[ ]:


# finding element for job search bar
search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g


# In[ ]:


# write on search bar
search_g.send_keys('sneakers')


# In[ ]:


search_button=driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
search_button


# In[ ]:


search_button=driver.find_element_by_class_name('L0Z3Pu')
search_button.click()


# In[ ]:


B_name=[]
Price=[]
P_desc=[]
Discount=[]


# In[ ]:


for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    discount=driver.find_elements_by_xpath("//div[@class='_3Ay6Sb']")
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
    for t in discount:
        Discount.append(t.text)
    Discount[:100]


# In[ ]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100])),print(len(Discount[:100]))


# In[ ]:


#Creating Dataframe
sun_gl=pd.DataFrame({})
sun_gl['Brand_name']=B_name[:100]
sun_gl['P_price']=Price[:100]
sun_gl['Pr_desc']=P_desc[:100]
sun_gl['P_discount']=Discount[:100]


# In[ ]:


sun_gl


# Q7

# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


url=" https://www.amazon.in "
driver.get(url)


# In[ ]:


# finding element for job search bar
search_g= driver.find_element_by_xpath("//input[@type='text']")
search_g


# In[ ]:


# write on search bar
search_g.send_keys('Laptop')


# In[ ]:


search_btn=driver.find_element_by_xpath("//input[@id='nav-search-submit-button']")
search_btn


# In[ ]:


Title=[]
Price=[]
Rating=[]


# In[ ]:


for i in range(3):
    b_name=driver.find_elements_by_xpath("//div[@class='_2WkVRV']")
    p_desc=driver.find_elements_by_xpath("//a[@class='IRpwTa']")
    price =driver.find_elements_by_xpath("//div[@class='_25b18c']")
    
    
    for j  in b_name:
        Title.append(j.text)
    Title[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 


# In[ ]:


Q8


# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


#Webpage
driver.get("https://www.azquotes.com/")


# In[ ]:


#Top Quotes
top_quotes_button = driver.find_element(By.LINK_TEXT, "Top Quotes")
top_quotes_button.click()


# In[ ]:


#scrape data
quotes = driver.find_elements(By.CSS_SELECTOR, ".title a")
authors = driver.find_elements(By.CSS_SELECTOR, ".author a")
types = driver.find_elements(By.CSS_SELECTOR, ".kw-box a")

for quote, author, quote_type in zip(quotes, authors, types):
print("Quote:", quote.text)
print("Author:", author.text)
print("Type of Quote:", quote_type.text)
print()


# In[ ]:


driver.quit()


# Q9

# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


#Webpage
driver.get('https://www.jagranjosh.com/')


# In[ ]:


#Click on GK Option
gk_option = driver.find_element_by_link_text('GK')
gk_option.click()


# In[ ]:


#List of all Prime Ministers of India
pm_option = driver.find_element_by_link_text('List of all Prime Ministers of India')
pm_option.click()


# In[ ]:


#Scrape Data
data = []
table = driver.find_element_by_xpath('//table[@class="table4"]')
rows = table.find_elements_by_tag_name('tr')
for row in rows:
  cols = row.find_elements_by_tag_name('td')
  if len(cols) == 4:
  name = cols[0].text
  born_dead = cols[1].text
  term_of_office = cols[2].text
  remarks = cols[3].text
  data.append([name, born_dead, term_of_office, remarks])


# In[ ]:


#Create Dataframe
df = pd.DataFrame(data, columns=['Name', 'Born-Dead', 'Term of Office', 'Remarks'])


# In[ ]:


driver.quit()


# Q10

# In[ ]:


#connecting the web driver
driver = webdriver.Chrome(r"C:\Users\vivek\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


#Webpage
driver.get('https://www.motor1.com/')


# In[ ]:


#Type in search box
search_bar = driver.find_element_by_id('search-input')
search_bar.send_keys('50 most expensive cars')
search_bar.submit()


# In[ ]:


link = driver.find_element_by_link_text('50 Most Expensive Cars in the World')
link.click()


# In[ ]:


#Scrape data and create dataframe
car_names = driver.find_elements_by_xpath('//div[@class="article-content"]/h3')
car_prices = driver.find_elements_by_xpath('//div[@class="article-content"]/p')

data = []
for name, price in zip(car_names, car_prices):
  data.append([name.text, price.text])

df = pd.DataFrame(data, columns=['Car Name', 'Price'])
print(df)


# In[ ]:


driver.quit

