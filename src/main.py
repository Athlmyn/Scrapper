#Entry point
import requests
import bs4

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs4.BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end="\n"*2)

#print(page.content)
#print(soup.get_text())
#print(results.prettify())


