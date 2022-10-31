import urllib.request
from bs4 import BeautifulSoup
import re

class Definition:
	URL = 'https://sjp.pwn.pl/szukaj/'
	
	def __init__(self):
		pass
		
	def search(self, word):
		html = self.__download(word)
		meaning = self.__read_data(html)
		return meaning
		
	def __download(self, word):
		url = self.URL + word
		with urllib.request.urlopen(url) as web:
			html = web.read()
		return html

	def __read_data(self, web_data):
		dictionary = []
		soup = BeautifulSoup(web_data, 'html.parser')
		soup = soup.find(class_='wyniki sjp-so-wyniki sjp-so-anchor')
		soup = soup.find(class_='ribbon-element')
		title_tag = soup.find(class_='tytul')
		title = self.__strip(title_tag)
		title_tag.decompose()
		other = self.__strip(soup)
		return title, other

	def read_data(self, web_data):
		dictionary = []
		soup = BeautifulSoup(web_data, 'html.parser')
		soup = soup.find(class_='wyniki sjp-wyniki sjp-anchor')
		soup = soup.find(class_='ribbon-element')
		soup.span.decompose()
		if meaning := soup.find_all(class_='znacz'):
			dictionary = [self.__strip(element) for element in meaning]
		else:
			dictionary = [self.__strip(soup)]
		return dictionary

	def __strip(self, tag):
		text = tag.get_text(strip=True)
		start = text.find('«')
		end = text.find('»')
		text = text.replace('«', ' ').replace('»', '.').strip()
		return text
		

if __name__ == '__main__':
	d = Definition()
	test = d.search('defenestracja')
	print(test)
