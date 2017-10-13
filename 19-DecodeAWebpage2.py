import requests
from bs4 import BeautifulSoup


def parse_paragraph (url):
	paragraphs = []
	website_request = requests.get(url)
	website_content = BeautifulSoup(website_request.text, "html.parser")
	
	for paragraph in website_content.find_all('p'):
		if (paragraph.string != None):
			paragraphs.append(paragraph.string.strip())

	return paragraphs

def write_file (paragraphs):
    with open("19_Exercise.txt", "w") as textfile:
	    for paragraph in paragraphs:
	        textfile.write(paragraph + "\n")

if __name__ == "__main__":
	url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
	write_file(parse_paragraph(url))

input()