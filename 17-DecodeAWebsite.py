"""
Exercise 17: Decode a Website

Use the BeautifulSoup and requests Python packages 
	to print out a list of all the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup

website_request = requests.get('http://www.nytimes.com/')
website_content = BeautifulSoup(website_request.text, "html.parser")

print("New York Times headlines: ")
for title in website_content.find_all('h2', {'class' : 'story-heading'}):
	if (title.string != None):
		print(title.string.strip())

input()