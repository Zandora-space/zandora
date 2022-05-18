import requests
from bs4 import BeautifulSoup
import random
from time import sleep
#import scrape

keyword = input("Enter the Keyword: ")
n_pages = int(input("Enter no. of Pages to Scrape: "))
result = []
html_result = []
descriptions = []
q = ['"@gmail.com" site:facebook.com','"@gmail.com" site:twitter.com','"@gmail.com" site:linkedin.com','"@gmail.com" site:instagram.com']

queries = []

for value in q:
    queries.append(keyword + ' ' + str(value))

#query = '"email marketing" "@gmail.com" site:linkedin.com'


user_agent_list = [
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]
for _ in user_agent_list:
    user_agent = random.choice(user_agent_list)

headers = {'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def serp_data():
  for query in queries:
    for page in range(1, n_pages):
        url = "https://www.google.com/search?q=" + \
            query + "&start=" + str((page - 1) * 10) + "&num=100"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        texts = soup.findAll(text=True)
        description=soup.find_all('div', class_="VwiC3b")
        result.append(texts)
        html_result.append(soup)
        print("Scraping Query: ", query,"page number: ", page)
        for d in description:
            descriptions.append(d.text)
        sleep(5)
        
def serp_save_data():
    with open(r"data.txt", 'w') as output:
        for x in descriptions:
            output.write(str(x) + '\n')
            
def serp_save_html_data():
    with open(r"data.html", 'w') as output:
        for x in html_result:
            output.write(str(x) + '\n')

            
serp_data()
serp_save_data()
serp_save_html_data()
print(descriptions)

#search=soup.find_all('div', class_="yuRUbf")
#for h in search:
#    links.append(h.a.get('href'))
#    titles.append(h.a.h3.text)
