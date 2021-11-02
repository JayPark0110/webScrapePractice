import requests  #scrap from web site
from bs4 import BeautifulSoup  #data extractor for HTML

LIMIT = 10
URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&l=%EC%84%9C%EC%9A%B8&start={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')  # whole HTML
    pagination = soup.find("div",
                           {"class": "pagination"})  # find div ~ in HTML

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "jobTitle"})
    title = title.find("span", title=True).string
    company = html.find("span", {"class": "companyName"}).string
    location = html.find("div", {"class": "companyLocation"}).string
    job_id = html["data-jk"]
    return {
        'title':
        title,
        'company':
        company,
        'location':
        location,
        'link':
        f"https://kr.indeed.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%A7%81-%EC%B7%A8%EC%97%85-%EC%84%9C%EC%9A%B8-%EC%A7%80%EC%97%AD?vjk={job_id}"
    }


def extract_jobs(last_page):    
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("a", {"class": "tapItem"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
