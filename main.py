#pylint:disable=R0201
#pylint:disable=W0106
import urllib.request
from bs4 import BeautifulSoup


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
		soup = BeautifulSoup(web_data,  'html.parser')
		soup = soup.find_all(class_='entry')
		dictionary = {}
		for entry in soup:
			if meaning:= entry.find_all(class_ = 'znacz'):
				title = entry.find(class_ = 'tytul')
				dictionary[title.text] = [:element.text.strip() for element in meaning]
		return dictionary
		

if __name__ == '__main__':
	d = Definition()
	test = d.search('test')
	print(test)
	