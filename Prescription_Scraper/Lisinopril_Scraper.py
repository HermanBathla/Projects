##This scraper creates a table of all doctors who have 
##prescribed Lisinopril based on information from the 
##ProPublica list, avaliable at projects.propublica.org/checkup/drugs/190

import csv
import requests
import bs4


list_of_rows = []

#There are multiple pages of tables on the website, 
#so a for loop is needed to iterate through each page.
for page in range(1, 5):
	url = 'http://projects.propublica.org/checkup/drugs/190?page=%d&sort=drug_claims' % (page)
	response = requests.get(url)
	html = response.content

	soup = bs4.BeautifulSoup(html, "lxml")
	table = soup.find('table', attrs = {'id': 'providers'})
	table = table.find('tbody')
	for row in table.findAll('tr')[1:]:
		list_of_cells = []
		for cell in row.findAll('td'):
			text = cell.text
			text = text.replace('Claims Filled', '')
			text = text.replace('\n', '')
			if text != '':
				list_of_cells.append(text)
		list_of_rows.append(list_of_cells)
		print(list_of_rows)
		print('end')


outfile = open("./physicians.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Provider", "Medicare Claims", "City", "State"])
writer.writerows(list_of_rows)