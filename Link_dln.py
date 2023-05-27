import time

import pyshorteners
import json
from modules import *
import pandas as pd

#new_company=[]
new_jobs_title=[]
new_jobs_link=[]
def scrape_and_print_jobs():
    def shortenurl(url):
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
    def print_job_details(company_names, job_titles, job_links):
        # print("Company Names:")
        # if len(company_names) == 0:
        #     print("No company names found.")
        # else:
        #     new_company.append(company_names)

        #print("\nJob Titles:")
        if len(job_titles) == 0:
            print("No job titles found.")
        else:
            new_jobs_title.append(job_titles)
        Jobs = []
        #print("\nJob Links:")
        #print(job_links)
        for link in job_links:
            shortened_link = shortenurl(link)
            Jobs.append(shortened_link)
        new_jobs_link.append(Jobs)


    y = driver.find_elements(By.CSS_SELECTOR, '.results-context-header__job-count')[0].text
    n = pd.to_numeric(y)

    i = 2
    while i <= int((n + 200) / 25) + 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1

        try:
            send = driver.find_element_by_xpath("//button[@aria-label='Load more results']")
            driver.execute_script("arguments[0].click();", send)
            time.sleep(2)
        except:
            pass
            time.sleep(2)

    companyname = []
    titlename = []

    try:
        for i in range(n):
            company = driver.find_elements(By.CSS_SELECTOR, '.base-search-card__subtitle')[i].text
            companyname.append(company)
    except:
        pass  # Set companyname list to empty if no company names are found

    try:
        for i in range(n):
            title = driver.find_elements(By.CSS_SELECTOR, '.base-search-card__title')[i].text
            titlename.append(title)
    except:
        pass  # Set titlename list to empty if no job titles are found

    jobList = driver.find_elements(By.CSS_SELECTOR, '.base-card__full-link')
    hrefList = []

    for e in jobList:
        hrefList.append(e.get_attribute('href'))

    driver.quit()

    print_job_details(companyname, titlename, hrefList)

# Call the function to scrape and print job details
scrape_and_print_jobs()

# print(new_company)
# print(new_jobs_title)
# print(new_jobs_link)
job_data = {}

for title_list, url_list in zip(new_jobs_title, new_jobs_link):
    for title, url in zip(title_list, url_list):
        job_data[title] = url

json_data = json.dumps(job_data, indent=4)

with open('job_data.json', 'w') as file:
    file.write(json_data)
time.sleep(60)
from SQL_Code import *
insert_json_into_database()
time.sleep(5)
from twillio_automation import *
time.sleep(3)
Job_links()
