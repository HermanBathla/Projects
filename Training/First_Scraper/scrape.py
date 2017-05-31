import requests
import bs4

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = bs4.BeautifulSoup(html)
print(soup.prettify())