import csv
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
	print("Hello World")

	req = requests.get("http://www.shilladfs.com/estore/kr/ko/e/bestshop?type=selling&mc=1#url")
	html = req.text

	soup = BeautifulSoup(html, 'html.parser')

	my_titles = soup.select(
		'#best_selling1 > div.best_box > ul > li.list_01 > div > div.product_off > div.pr_info > div.price > span.sale'
		)

	
	f = open('output.csv', 'w', newline='')
	wr = csv.writer(f)

	for title in my_titles:
		wr.writerow([1, title.text, "데이빗1"])
		wr.writerow([2, title.text, "데이빗2"])
		print(title.text)

	f.close()
