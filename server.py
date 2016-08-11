from flask import Flask, request, render_template, jsonify
from markov import Markovify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def post_info():

    new_person = Markovify(3,50,"negative")
    new_person.import_text('06-22-16-On_hilary.txt', 'speech')
    new_person.import_text('08-08-16-2nd_amend_speech.txt', 'speech')
    new_person.import_text('07-28-16-RNC.txt', 'speech')
    new_person.sentiment_filter('speech')
    new_person.create_dictionary()
    new_person.generate_text()
    return render_template('index.html', output=new_person.output)

if __name__ == "__main__":
    app.run(debug = True)