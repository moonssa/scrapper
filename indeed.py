
from compileall import compile_path
from unittest import TestLoader
from xmlrpc.client import FastMarshaller
import requests;
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}";

def extra_indeed_pages():
    result = requests.get(URL);

    soup = BeautifulSoup(result.text, "html.parser");


    pagination = soup.find("ul", {"class":"pagination-list"});
    # print(pagination);

    pages = pagination.find_all("a")

    # print(pages)

    spans=[]
    for page in pages:
        spans.append(page.find("span").string)

    spans = list(map(int,spans[0:-1]))

    max_page = spans[-1];

    return max_page;

# def extract_job(html):
#     title = html.find("h2", {"class":"jobTitle"}).find("span").string;
#     company = html.find("span", {"class": "companyName"}).string
#     location= html.find("div", {"class": "companyLocation"}).string
#     id = html["data-jk"]
#     print(id)
        
#     print(title, "/" , company, "/", location)
#     return{'title': title , 'company': company, 'location': location}


def extract_job(html):
    title = html.find("a", {"class":"jobTitle"}).find("span").string;
    company = html.find("span", {"class": "companyName"}).string
    location= html.find("div", {"class": "companyLocation"}).string
    id = html["data-jk"]
    print(id)
        
    print(title, "/" , company, "/", location)
    return{'title': title , 'company': company, 'location': location}


def extract_indeed_jobs(last_page):
    jobs=[]
    last_page=1
    for page in range(last_page):
        print (f'Scrapping page  # {page+1}')
        url = f"&start={page*LIMIT}"
        result = requests.get(f"{URL}{url}")
        soup = BeautifulSoup(result.text, "html.parser");
        #job_cards =soup.find("div", {"class": "mosaic-provider-jobcards"})

        job_cards =soup.find("div", {"id": "mosaic-provider-jobcards"}).find_all('a', recursive=False)
   
        for x , job_card in enumerate(job_cards):
            #print(job_card)
            print(job_card["data-jk"])
            print(job_card.find('h2',{"class":"jobTitle"}).find("span", recursive=False).string)
            print(job_card.find("span", {"class": "companyName"}).string)
            print(job_card.find("div", {"class": "companyLocation"}).string)
            print(x, "===")
          
      
    return jobs


# def extract_indeed_jobs(last_page):
#     jobs=[]
#     last_page=1
#     for page in range(last_page):
#         print (f'Scrapping page  # {page+1}')
#         url = f"&start={page*LIMIT}"
#         result = requests.get(f"{URL}{url}")
#         soup = BeautifulSoup(result.text, "html.parser");
#         job_cards =soup.find_all("table", {"class": "jobCard_mainContent"})
#         for job_card in job_cards:
#             job = job_card.find("td", {"class":"resultContent"})
#             jobs.append(extract_job(job))
#         # print(jobs)
#     return jobs
