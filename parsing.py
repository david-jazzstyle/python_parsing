import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
	print("Hello World")
	# req = urllib.request.Request("http://www.shilladfs.com/estore/kr/ko/e/bestshop?type=selling&mc=1#url");
	# data = urllib.request.urlopen(req).read()	
	# bs = BeautifulSoup(data, 'html.parser')
	# l = bs.find('li', {'class' : 'list_01'})

	req = requests.get("http://www.shilladfs.com/estore/kr/ko/e/bestshop?type=selling&mc=1#url")
	html = req.text
	# header = req.headers
	# status = req.status_code
	# is_ok = req.ok
	soup = BeautifulSoup(html, 'html.parser')
	# my_prices = soup.select(
 #    ' > a'
 #    )

	my_titles = soup.select(
		'#best_selling1 > div.best_box > ul > li.list_01 > div > div.product_off > div.pr_info > div.price > span.sale'
		)

	for title in my_titles:
		print(title.text)
 		# print(title.get('href'))
	
	# list1 = soup.find('li', {'class' : 'list_01'})
	# list2 = soup.find('li', {'class' : 'list_02'})

	# soup_price = BeautifulSoup(list1, 'html.parser')

	# price1 = soup_price.find(('span', {'class' : 'sale'}))

	# print(price1) 	

	# idx = 0
	# for s in l:
	# 	try:
	# 		print("%d : %s" % (idx, str(s)))
	# 	except UnicodeEncodeError:
	# 		print("Errror : %d" % (idx))
	# 	finally:
	# 		idx += 1