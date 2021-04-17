import requests
from bs4 import BeautifulSoup
import time

#make request to website
html = requests.get()
#The name of the website should be written between the parentheses and adjustments to html parser should be made accordingly.
c = html.content
soup = BeautifulSoup(c,'html.parser')

print('Write a skill you are unfamiliar with below.')
unfamiliar_skill = input('>')
lst = unfamiliar_skill.split()
print(f'Filtering out {unfamiliar_skill}...')


jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    job_pub_day = job.find('span', class_ = 'sim-posted').text
    if 'few' in job_pub_day:
        job_skills = job.find('span', class_ = 'srp-skills').text.replace('  ','')
        unfamiliar_skill = unfamiliar_skill.replace('&','')
        names = []
        more_info = []
        for skill in lst:
            print(skill)
            if skill not in job_skills:
                names.append(job.h3.text.replace(' ',''))
                more_info.append(job.h2.a['href'])
                for i in range(len(names)):
                    print('=====================================b==')
                    print(f'Company name: {names[i]}')
                    print(f'Job Skill: {job_skills}')
                    print(f'Job Publication Date: {job_pub_day}')
                    print(f'More Info: {more_info[i]}')




