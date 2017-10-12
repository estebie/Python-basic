import requests
from bs4 import BeautifulSoup

website_request = requests.get('http://www.nytimes.com/')
website_content = BeautifulSoup(website_request.text, "html.parser")

print("New York Times headlines: ")
for title in website_content.find_all('h2', {'class' : 'story-heading'}):
	if (title.string != None):
		print(title.string.strip())

input()