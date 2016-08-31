from flask import Flask, request, render_template, jsonify
from markov import Markovify
import random
import markov.py

app = Flask(__name__)

trump = ['06-22-16-On_hilary.txt', '08-08-16-2nd_amend_speech.txt', '07-28-16-RNC.txt']
obama = ['01-20-09-Inaugural_address.txt', 'degrade_and_destroy_ISIL.txt']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def post_info():
    new_person = Markovify(int(request.form['n-grams']),int(request.form['out-length']),request.form['style'])
    if request.form['speaker'] == 'Trump':
        if request.form['type'] == 'Speech':
            new_person.corpus_speech = request.form['add']
            for i in range(len(trump)):
                file_locate = 'assets/trump/' + str(trump[i])
                new_person.import_speech(file_locate)
        elif request.form['type'] == 'Tweet':
            new_person.corpus_tweet = request.form['add']
            new_person.import_tweet('25073877')
    elif request.form['speaker'] == 'Obama':
        if request.form['type'] == 'Speech':
            new_person.corpus_speech = request.form['add']
            for i in range(len(obama)):
                file_locate = 'assets/obama/' + str(obama[i])
                new_person.import_speech(file_locate)
        elif request.form['type'] == 'Tweet':
            new_person.corpus_tweet = request.form['add']
            new_person.import_tweet('813286')
    new_person.sentiment_filter(request.form['type'])
    new_person.create_dictionary()
    new_person.generate_text()
    return render_template('index.html', output=new_person.output, speaker=request.form['speaker'])

if __name__ == "__main__":
    app.debug = True
    app.run()