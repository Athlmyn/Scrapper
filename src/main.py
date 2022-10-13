#Entry point
import requests
import bs4

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs4.BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

#print(page.content)
print(soup.get_text())

