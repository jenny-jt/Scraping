import requests
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime

# url = 'https://www.indeed.com/jobs?q=python&l=new+york'
url = 'https://www.linkedin.com/jobs/view/2165533703/?alternateChannel=search&refId=oZlHex62ZpQS%2BjOjDjDUBg%3D%3D&trackingId=hLNFWOL4P%2F21pZZVdkxyrA%3D%3D'
# url = 'https://www.linkedin.com/jobs/view/2406107518/?refId=CAHwyJXAZadoE9o%2FVbXbfw%3D%3D&trackingId=M6KQvLu%2FdNPuEHd1Ky%2FINw%3D%3D'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

job_title = soup.find(
    class_='topcard__title').text

company = soup.find(
    'a', class_='topcard__org-name-link topcard__flavor--black-link').text

job_description = soup.find('div', class_='show-more-less-html__markup').text

location = soup.find(
    'span', class_='topcard__flavor topcard__flavor--bullet').text

seniority_level = soup.find(
    'span', class_='job-criteria__text job-criteria__text--criteria').text

employment_type = soup.find(
    'ul', class_='job-criteria__list').find_all('li', class_='job-criteria__item')[1].find('span', class_='job-criteria__text job-criteria__text--criteria').text

posting_date = soup.find(
    'span', class_="topcard__flavor--metadata posted-time-ago__text").text

# TODO: use datetime to calculate actual calendar date that it was posted

print("Job Title: ", job_title)
print("Company: ", company)
print("Job Description: ", job_description)
print("Location: ", location)
print("Seniority Level: ", seniority_level)
print("Employment type: ", employment_type)
print("Posting Date: ", posting_date)

date = posting_date.strftime("%m-%d-%Y")
print(date)