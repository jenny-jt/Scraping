import requests
from pprint import pprint
from bs4 import BeautifulSoup

# url = 'https://www.indeed.com/jobs?q=python&l=new+york'
# url = 'https://www.linkedin.com/jobs/view/2165533703/?alternateChannel=search&refId=oZlHex62ZpQS%2BjOjDjDUBg%3D%3D&trackingId=hLNFWOL4P%2F21pZZVdkxyrA%3D%3D'
url = 'https://www.linkedin.com/jobs/view/2406107518/?refId=CAHwyJXAZadoE9o%2FVbXbfw%3D%3D&trackingId=M6KQvLu%2FdNPuEHd1Ky%2FINw%3D%3D'

page = requests.get(url)
# print(page.content[:100])
# loc = str(page.content).find('job')

soup = BeautifulSoup(page.content, 'html.parser')

job_title = soup.find(
    class_='topcard__title').text

company = soup.find(
    'a', class_='topcard__org-name-link topcard__flavor--black-link').text

job_description = soup.find('div', class_='show-more-less-html__markup').text

print(job_title)
print(company)
print(job_description)

# print(div.get('class'))


# print(job_cards)

# print(test.prettify())
# print(job_title.prettify())
# print(job_description.prettify())
