import csv
import requests
import bs4

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'
response = requests.get(url)
html = response.content

soup = bs4.BeautifulSoup(html, "lxml")
table = soup.find('tbody', attrs = {'class': 'stripe'})

print(table)

list_of_rows = []
for row in table.findAll('tr')[1:]:
	list_of_cells = []
	for cell in row.findAll('td'):
		print(cell)
		print('end')
		text = cell.text.replace('Details', '')
		text = text.replace('\n\xa0\n', '')
		if text != '':
			list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race",  \
"Age", "City", "State"])
writer.writerows(list_of_rows)