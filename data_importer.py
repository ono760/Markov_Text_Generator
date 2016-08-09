import urllib
from bs4 import BeautifulSoup
import nltk, re, pprint

url = 'http://www.cnn.com/2016/08/08/politics/donald-trump-hillary-clinton-economic-plans/index.html'
html = urllib.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, 'html.parser')

# This section would depend on what where the text is on the page
relevant_raw = raw.find_all(class_='zn-body__paragraph')
relevant_text = ''
for obj in relevant_raw:
	relevant_text += obj.text

# tokens = nltk.word_tokenize(relevant_text)
sent = nltk.sent_tokenize(relevant_text)
# pos = nltk.pos_tag(nltk.word_tokenize(sent[0]))
# bigram = nltk.bigrams(tokens[10:20])
# taggin POS
# fd = nltk.FreqDist(tag for (word,tag) in pos)
# print fd.tabulate()

# list_bi = list(bigram)

sent = [nltk.word_tokenize(i) for i in sent]
sent = [nltk.pos_tag(i) for i in sent]
print sent