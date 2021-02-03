import requests
from pprint import pprint
from bs4 import BeautifulSoup

# url = 'https://www.indeed.com/jobs?q=python&l=new+york'
url ='https://www.linkedin.com/jobs/view/2165533703/?alternateChannel=search&refId=oZlHex62ZpQS%2BjOjDjDUBg%3D%3D&trackingId=hLNFWOL4P%2F21pZZVdkxyrA%3D%3D'

page = requests.get(url)
# print(page.content[:100])
# loc = str(page.content).find('job')

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.get_text())
# test = soup.find(id="jobsearch_nav")

# job_cards = soup.find_all(class_="jobsearch-SerpJobCard")
# job_cards = soup.get_text("job")
# job_cards = soup.find_all('a')

for job_title in soup.find_all('div'):
    # if job_title.get('class') ==
    print(job_title.get('class'))



# print(job_cards)

# print(test.prettify())
# print(job_title.prettify())
# print(job_description.prettify())
