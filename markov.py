import nltk,re, pprint, string, twython, random
nltk.data.path.append("./nltk_data")
from nltk import sent_tokenize, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from env import CONSUMER_KEY, CONSUMER_SECRET

class Markovify:

    def __init__(self, chain_length, out_length, sentiment):
        self.chain_length = chain_length
        self.out_length = out_length
        self.corpus_speech = ''
        self.corpus_tweet = ''
        self.tokens = []
        self.sent_speech = []
        self.sent_tweet = []
        self.sentiment = sentiment
        self.dictionary = {}
        self.output = ''

    def import_speech(self, text):
        with open(text, 'r') as original:
            temp_speech = original.read()
            self.corpus_speech += unicode(temp_speech, 'utf-8')
        self.sent_speech = sent_tokenize(self.corpus_speech)

    def import_tweet(self,user_id):
        user = user_id
        twitter = twython.Twython(CONSUMER_KEY,CONSUMER_SECRET)
        user_timeline = twitter.get_user_timeline(user_id = user, include_rts = False, count = 500)
        for tweet in user_timeline:
            self.corpus_tweet += tweet['text']
        p = re.compile(ur'([@#].*?\s)')
        p2 = re.compile(ur'https?:[^\s]+', re.IGNORECASE)
        self.corpus_tweet=(re.sub(p,'',self.corpus_tweet))
        self.corpus_tweet=(re.sub(p2,'',self.corpus_tweet))
        self.sent_tweet = sent_tokenize(self.corpus_tweet)

    def sentiment_filter(self, text_type):
        if self.sentiment == 'positive':
            sentiment_factor = .3
            sentiment = 'pos'
        elif self.sentiment == 'negative':
            sentiment_factor = .3
            sentiment = 'neg'
        elif self.sentiment == 'neutral':
            sentiment_factor = .3
            sentiment = 'neu'

        if text_type == 'Speech':
            text_type = self.corpus_speech
        elif text_type == 'Tweet':
            text_type = self.corpus_tweet

        sentences = sent_tokenize(text_type)
        sid = SentimentIntensityAnalyzer()
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            if ss[sentiment] > sentiment_factor:
                self.tokens += word_tokenize(sentence)

    def create_dictionary(self):

        for i in range(len(self.tokens) - (self.chain_length - 1)):
            cur_key = []
            for j in range(self.chain_length - 1):
                cur_key.append(self.tokens[i + j])
            cur_key = tuple(cur_key)
            if cur_key in self.dictionary:
                self.dictionary[cur_key].append(self.tokens[i + self.chain_length - 1])
            else:
                self.dictionary[cur_key] = [self.tokens[i + self.chain_length - 1]]

    def generate_text(self):

        output_text = []
        start_words = []

        for word in self.tokens:
            if word[0].upper() + word[1:].lower() == word:
                start_words.append(word)
                start_words = [''.join(c for c in s if c not in string.punctuation) for s in start_words]
                start_words = [s for s in start_words if s]
        first_word = random.choice(start_words)
        cache = [first_word]
        for i, word in enumerate(self.tokens):
            if word == first_word:
                for j in range(self.chain_length - 2):
                    cache.append(self.tokens[i + j + 1])
                break
        output_text += cache

        for i in range(self.out_length - (self.chain_length - 1)):
            for key in self.dictionary:
                if tuple(cache) == key:
                    next_word = random.choice(self.dictionary[key])
                    output_text.append(next_word)
                    cache.append(next_word)
                    cache.pop(0)
                    break
        self.output = (' '.join(output_text) + '.')
