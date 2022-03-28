import requests;
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}";

def extra_indeed_pages():
    result = requests.get(URL);

    soup = BeautifulSoup(result.text, "html.parser");


    pagination = soup.find("ul", {"class":"pagination-list"});
    print(pagination);

    pages = pagination.find_all("a")

    print(pages)

    spans=[]
    for page in pages:
        spans.append(page.find("span").string)

    spans = list(map(int,spans[0:-1]))

    max_page = spans[-1];

    return max_page;


def extract_indeed_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        url = f"&start={page*LIMIT}"
        result = requests.get(f"{URL}{url}")
        print(result.status_code)
    return jobs
