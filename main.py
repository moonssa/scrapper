import requests;
from bs4 import BeautifulSoup

result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50");

indeed_soup = BeautifulSoup(result.text, "html.parser");
#print(indeed_soup);

pagination = indeed_soup.find("ul", {"class":"pagination-list"});
print(pagination);

pages = pagination.find_all("a")

print(pages)

spans=[]
for page in pages:
    print(page);
    print("*********");
    print(page.find("span").string)
    spans.append(page.find("span").string)

print(spans);
spans = list(map(int,spans[0:-1]))

max_page = spans[-1];

for n in range(max_page):
    print(f"start")






