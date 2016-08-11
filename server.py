from flask import Flask, request, render_template, jsonify
from markov import Markovify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def post_info():
    print request.form['out-length']
    print int(request.form['out-length'])
    new_person = Markovify(int(request.form['n-grams']),int(request.form['out-length']),request.form['style'])
    new_person.import_speech('06-22-16-On_hilary.txt', 'speech')
    new_person.import_speech('08-08-16-2nd_amend_speech.txt', 'speech')
    new_person.import_speech('07-28-16-RNC.txt', 'speech')
    new_person.sentiment_filter('speech')
    new_person.create_dictionary()
    new_person.generate_text()
    return render_template('index.html', output=new_person.output)

if __name__ == "__main__":
    app.run(debug = True)