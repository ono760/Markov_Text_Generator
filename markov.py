import nltk, re, pprint
# from nltk import tokenize
from nltk import sent_tokenize, word_tokenize
# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import subjectivity
# from nltk.sentiment import SentimentAnalyzer
# from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Markovify:

    def __init__(self, chain_length, out_length, sentiment):
        self.chain_length = chain_length
        self.out_length = out_length

        self.corpus_speech = ''
        self.corpus_tweet = ''
       
        self.tokens_speech = []
        self.tokens_tweet = []
        self.tokens = []

        self.sent_speech = []
        self.sent_tweet = []

        self.pos_speech = []
        self.pos_tweet = []

        self.sentiment = sentiment

        self.dictionary = {}

        self.nltk_text = None
    
    def import_text(self, text, text_type):

        if text_type == 'speech':
            with open(text, 'r') as original:
                temp_speech = original.read()
                self.corpus_speech += unicode(temp_speech, 'utf-8')
            self.sent_speech = sent_tokenize(self.corpus_speech)
            self.tokens_speech = word_tokenize(self.corpus_speech)
            self.pos_speech = nltk.pos_tag(self.tokens_speech)
            self.words_speech = self.corpus_speech.split(' ')

        elif text_type == 'tweet':
            with open(text, 'r') as original:
                temp_tweet = original.read()
                self.corpus_tweet += unicode(temp_tweet, 'utf-8')
            self.sent_tweet = sent_tokenize(self.corpus_tweet)
            self.tokens_tweet = word_tokenize(self.corpus_tweet)
            self.pos_tweet = nltk.pos_tag(self.tokens_tweet)
            self.words_tweet = self.corpus_tweet.split(' ')

    def sentiment_filter(self, text_type):
        if self.sentiment == 'positive':
            sentiment_factor = .5
            sentiment = 'pos'
        elif self.sentiment == 'negative':
            sentiment_factor = .1
            sentiment = 'neg'
        elif self.sentiment == 'neutral':
            sentiment_factor = .5
            sentiment = 'neu'

        if text_type == 'speech':
            text_type = self.corpus_speech
        elif text_type == 'tweet':
            text_type = self.corpus_tweet

        sentences = sent_tokenize(text_type)
        sid = SentimentIntensityAnalyzer()
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            if ss[sentiment] > sentiment_factor:
                self.tokens += word_tokenize(sentence)         

    def create_dictionary(self):
        # to create the words we may want to adjust between tweets and speech
        # self.tokens = self.tokens_tweet + self.tokens_speech

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
        import random
        output_text = []
        start_words = []

        # creates a list of words to start the output text (consider
        # refactoring to have only words where prev is .)
        for word in self.tokens:
            if word[0].upper() + word[1:].lower() == word:
                start_words.append(word)

        first_word_idx = int(len(start_words) * random.random())
        first_word = start_words[first_word_idx]

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
        print(' '.join(output_text))

trump = Markovify(3, 50, 'negative')
trump.import_text('06-22-16-On_hilary.txt', 'speech')
trump.import_text('08-08-16-2nd_amend_speech.txt', 'speech')
trump.import_text('07-28-16-RNC.txt', 'speech')
trump.sentiment_filter('speech')
trump.create_dictionary()
trump.generate_text()
