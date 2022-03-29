from xmlrpc.client import FastMarshaller
import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python"


def extra_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "s-pagination"})

    pages = pagination.find_all("span")
    spans = []
    for page in pages:
        spans.append(page.string)

    max_page = int(spans[-2])
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find(
        "h3", {"class": "fs-body1"}).find_all("span", recursive=False)

    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]

    return{'title': title, 'company': company, 'location': location,
           'apply_link': f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        print(f'SO  Scrapping page  # {page+1}')
        url = f"&pg={page}"
        result = requests.get(f"{URL}{url}")
        soup = BeautifulSoup(result.text, "html.parser")

        job_cards = soup.find_all("div", {"class": "-job"})

        for job_card in job_cards:
            job = extract_job(job_card)
            jobs.append(job)

    return jobs


def get_jobs():
    max_page = extra_pages()
    jobs = extract_jobs(max_page)

    return jobs
