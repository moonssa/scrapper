from indeed import extra_indeed_pages, extract_indeed_jobs


max_page = extra_indeed_pages()
print(max_page);

# for n in range(max_page):
#     print(f"start")

extract_indeed_jobs(max_page)





