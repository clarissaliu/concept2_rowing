import requests
from bs4 import BeautifulSoup
import json

all_data = []

page_counter = 1

while page_counter <= 57:
	url = f'https://log.concept2.com/rankings/2020/rower/100?gender=m&page={page_counter}'
	r = requests.get(url)
	r.encoding = 'utf-8'
	soup = BeautifulSoup(r.text, features='html.parser')


	main_table = soup.find('section', {'class':'content'})
	main_table = main_table.find('tbody')

	all_rows = main_table.find_all('tr')
	
	for row in all_rows:

		rank = None
		name = None
		age = None
		location = None
		country = None
		affiliation = None
		time = None
		row_type = None
		verified = None
		profile_url = None

		person_data = list(row.find_all('td'))


		rank = person_data[0].text
		name = person_data[1].text
		age = person_data[2].text
		location = person_data[3].text
		country = person_data[4].text
		affiliation = person_data[5].text
		time = person_data[6].text
		row_type = person_data[7].text
		verified = person_data[8].text
		profile_url = row.find('a')['href']

		all_data.append({
			'rank': rank,
			'name': name,
			'age': age,
			'location': location,
			'country': country,
			'affiliation': affiliation,
			'time': time,
			'type': row_type,
			'verified': verified,
			'profile url': profile_url,
			'gender': 'male',
			'distance': 100
			})
	
	with open('100m_data_male.json','w', encoding='utf-8') as outfile:
		json.dump(all_data,outfile,indent=2,ensure_ascii=False)	

	print(page_counter)
	page_counter+=1
	