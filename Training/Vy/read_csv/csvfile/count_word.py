import requests
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# you must install pandas, beautifulSoup, request, wordcloud before you run file.py
import matplotlib.pyplot as plt
# this function is craw data from vietnamnet.vb for giving texting.
def read_data():
    data = pd.read_csv('../data_csv/misubishi.csv')
    data_table = data.dropna()

    print(data_table['Content'].head())
    content_business = ','.join(data_table['Content'])
    count_word = WordCloud().process_text(content_business)
    word, frequently = count_word.keys(), count_word.values()
    count_word = pd.DataFrame([word, frequently]).T
    count_word.columns = ['word', 'frequently']
    count_word = count_word.sort_values(by = 'frequently', ascending = False)
    print(count_word)
data = read_data()
def craw_data():
	url = 'https://vietnamnet.vn/vn/oto-xe-may/top-10-xe-ban-chay-thang-3-mitsubishi-xpander-toyota-innova-tut-hang-632602.html'
	req = requests.get(url)
	html_soup = BeautifulSoup(req.content, 'html.parser')
	content = html_soup.select("#ArticleContent p")
	content_business = []
	for i in content:
		content_business.append(i.text)
	content_business = ','.join(content_business)
	return content_business
# this function is count word repetition from text
def count_word(content_business):
	count_word = WordCloud().process_text(content_business)
	word, frequently = count_word.keys(), count_word.values()
	count_word = pd.DataFrame([word, frequently]).T
	count_word.columns = ['word', 'frequently']
	count_word = count_word.sort_values(by = 'frequently', ascending = False)
	return count_word
# display cloudword
def display_cloudword(content_business):
	wordcloud = WordCloud(max_font_size=50, max_words=40, background_color="white").generate(content_business)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()
# content_business = craw_data()
# count_word = count_word(content_business)
# # print count_word repetition
# print(count_word)
# cloudword = display_cloudword(content_business)
