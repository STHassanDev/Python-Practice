import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
Typical format of a html table:

<table>
  <tr> 
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

"""

url = "https://www.ibm.com"

data = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

soup.prettify # Will return the entire html of the page.

for link in soup.find_all(href=True):
    (link.get('href')) # Will return all the links on the page

# Let's try scraping from tables 
    
url = url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

table = soup.find('table') # in html table is represented by the tag <table>

for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    # print("{}--->{}".format(color_name,color_code))

# Webscraping tables using pandas dataframe
    
url = "https://en.wikipedia.org/wiki/World_population"

data = requests.get(url).text

soup = BeautifulSoup(data,'html.parser')

tables = soup.find_all('table') # 29 tables in total (As of the last day of 2023)

for i,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = i
ours = tables[table_index]

print(ours.prettify)

population_data = pd.DataFrame(columns=["Rank","Country","Population","Area","Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        rank = col[0].text
        country = col[1].text.strip()
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data=pd.concat([population_data,pd.DataFrame({"Rank":[rank], "Country":[country], "Population":[population],
                                                                  "Area":[area], "Density":[density]})], ignore_index=True)

population_data

# Webscraping tables into a dataframe using beautiful soup and read html

#print(pd.read_html(url, flavor="bs4"))

