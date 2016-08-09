import nltk, re, pprint
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Markovify:

    def __init__(self, chain_length, out_length):
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

        self.dictionary = {}

        self.nltk_text = None
        

    def import_text(self, text, text_type):

        if text_type == 'speech':
			with open(text, 'r') as original:
				self.corpus_speech += original.read()
				self.corpus_speech = unicode(self.corpus_speech, 'utf-8')
			self.sent_speech = sent_tokenize(self.corpus_speech)
			self.tokens_speech = word_tokenize(self.corpus_speech)
			self.pos_speech = nltk.pos_tag(self.tokens_speech)
			self.words_speech = self.corpus_speech.split(' ')

        elif text_type == 'tweet':
			with open(text, 'r') as original:
				self.corpus_tweet += original.read()
				self.corpus_tweet = unicode(self.corpus_tweet, 'utf-8')
			self.sent_tweet = sent_tokenize(self.corpus_tweet)
			self.tokens_tweet = word_tokenize(self.corpus_tweet)
			self.pos_tweet = nltk.pos_tag(self.tokens_tweet)
			self.words_tweet = self.corpus_tweet.split(' ')
			
		# self.nltk_text = nltk.Text(self.tokens)

    def create_dictionary(self):

    	# to create the words we may want to adjust between tweets and speech
    	self.tokens = self.tokens_tweet + self.tokens_speech

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


    def sentiment_analysis(self):
        n_instances = 100
        subj_docs = [(sent, 'subj') for sent in subjectivity.sents(
            categories='subj')[:n_instances]]
        obj_docs = [(sent, 'obj')
                    for sent in subjectivity.sents(categories='obj')[:n_instances]]
        len(subj_docs), len(obj_docs)

        train_subj_docs = subj_docs[:80]
        test_subj_docs = subj_docs[80:100]
        train_obj_docs = obj_docs[:80]
        test_obj_docs = obj_docs[80:100]
        training_docs = train_subj_docs + train_obj_docs
        testing_docs = test_subj_docs + test_obj_docs
        sentim_analyzer = SentimentAnalyzer()
        all_words_neg = sentim_analyzer.all_words(
            [mark_negation(doc) for doc in training_docs])

        unigram_feats = sentim_analyzer.unigram_word_feats(
            all_words_neg, min_freq=4)
        len(unigram_feats)
        sentim_analyzer.add_feat_extractor(
            extract_unigram_feats, unigrams=unigram_feats)

        training_set = sentim_analyzer.apply_features(training_docs)
        test_set = sentim_analyzer.apply_features(testing_docs)

        trainer = NaiveBayesClassifier.train
        classifier = sentim_analyzer.train(trainer, training_set)

        for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
            print('{0}: {1}'.format(key, value))

        sentences = sent_tokenize(self.corpus_speech)

        sentences.extend(sentences)
        sid = SentimentIntensityAnalyzer()
        for sentence in sentences:
            print(sentence)
            ss = sid.polarity_scores(sentence)
            print(ss)
            for k in sorted(ss):
                print('{0}: {1},'.format(k, ss[k]))


trump = Markovify(3, 150)
trump.import_text('trump.txt', 'speech')
# trump.import_text('star_wars.txt')
trump.create_dictionary()
trump.generate_text()
trump.sentiment_analysis()
