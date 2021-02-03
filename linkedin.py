import requests
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

weeks_url = 'https://www.linkedin.com/jobs/view/2165533703/?alternateChannel=search&refId=oZlHex62ZpQS%2BjOjDjDUBg%3D%3D&trackingId=hLNFWOL4P%2F21pZZVdkxyrA%3D%3D'
# url = 'https://www.linkedin.com/jobs/view/2406107518/?refId=CAHwyJXAZadoE9o%2FVbXbfw%3D%3D&trackingId=M6KQvLu%2FdNPuEHd1Ky%2FINw%3D%3D'

hours_url = 'https://www.linkedin.com/jobs/view/2393605490/?alternateChannel=search&refId=pru82Hpg9w6tQ5Fw0jgnTw%3D%3D&trackingId=EVioOyXIQq0lsF%2BVoRc6Mw%3D%3D'
days_url = 'https://www.linkedin.com/jobs/view/2386792270/?alternateChannel=search&refId=pru82Hpg9w6tQ5Fw0jgnTw%3D%3D&trackingId=pzQzqtJZVkA0bpd70RQZQA%3D%3D&trk=flagship3_search_srp_jobs'

page = requests.get(hours_url)

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


def find_interval():
    interval = soup.find(
        'span', class_="topcard__flavor--metadata posted-time-ago__text posted-time-ago__text--new")
    if not interval:
        interval = soup.find('span', class_="topcard__flavor--metadata posted-time-ago__text")
    return interval.text


interval = find_interval()

#turned string into list [qt, unit, 'ago']
interval_list = interval.split()
unit = interval_list[1]
quantity = int(interval_list[0])

if unit == "days":
    delta = timedelta(days=quantity)
elif unit == "weeks":
    delta = timedelta(weeks=quantity)
elif unit == 'hours':
    delta = timedelta(hours=quantity)

posting_date = (datetime.now() - delta).strftime("%m-%d-%Y")

print("Job Title: ", job_title)
print("Company: ", company)
print("Job Description: ", job_description)
print("Location: ", location)
print("Seniority Level: ", seniority_level)
print("Employment type: ", employment_type)
print("Posting Date: ", posting_date)