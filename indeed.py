import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"


def extra_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("ul", {"class": "pagination-list"})

    pages = pagination.find_all("a")

    spans = []
    for page in pages:
        spans.append(page.find("span").string)

    spans = list(map(int, spans[0:-1]))
    max_page = spans[-1]
    return max_page


def extract_job(html):

    job_id = html["data-jk"]
    title = html.find('h2', {"class": "jobTitle"}).find(
        "span", recursive=False).string
    company = html.find("span", {"class": "companyName"}).string
    location = html.find("div", {"class": "companyLocation"}).string
    link = f"https://kr.indeed.com/jobs?q=python&l&vjk={job_id}"

    return{'title': title, 'company': company, 'location': location, 'apply_link': link}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Indeed  Scrapping page  # {page+1}')
        url = f"&start={page*LIMIT}"
        result = requests.get(f"{URL}{url}")
        soup = BeautifulSoup(result.text, "html.parser")

        job_cards = soup.find(
            "div", {"id": "mosaic-provider-jobcards"}).find_all('a', recursive=False)

        for x, job_card in enumerate(job_cards):
            jobs.append(extract_job(job_card))

    return jobs


def get_jobs():
    max_page = extra_pages()
    jobs = extract_jobs(max_page)

    return jobs
