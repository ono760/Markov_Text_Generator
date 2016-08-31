# Markov Random Text Generator
####Link:  [Q3Project](https://q2project.herokuapp.com/)
***
This web application is a Python implementation of a Markov text generator.

Markov Model: "A sequence of possible events in which the probability of each event only depends on the state attained in the previous
event."

A Markov Text Generator can be used to randomly generate somewhat realistic sentences using words from a text corpus. Words are joined together in sequence, with each new word being selected based on how often it follows the previous word in the source document.


Start with two consecutive words from the text. The last two words constitute the present state.
Generating next word is the markov transition. To generate the next word, look in the corpus, and find which words are present after the given two words. Choose one of them randomly.
Repeat 2, until text of required size is generated.

The larger text we choose, the more choices are there at each transition, and a better looking text is generated.
The state can be set to depend on one word, two words, or any number of words. As the number of words in each state increases, the generated text becomes less random.

How is this a markov algorithm?
The last two words are the current state.
Next word depends on last two words only, or on present state only.
The next word is randomly chosen from a statistical model of the corpus.

The results are often just nonsense, but at times can be strangely poetic


This is a very simple Markov chain text generator. Try it below by entering some text or by selecting one of the pre-selected texts available.

This converter will read your input text and build a probability function. This function indicates how likely a certain word follows another given word. It will then randomly generate a text by using this probability function.

This program builds Markov models using the Markovify library, storing the models as lists, allowing the cache to save results for
later use and produce more natural-like sentences. Our models are created using large corpora texts (Donal Trump Obama speeches and Tweets) and generates positive or negative text from that text corpus. For sentiment analysis, we used Python's NLTK (Natural Language Toolkit) 



| Technologies Used    |
| -------------------- |
| Python 2.7    		  	|
| CSS (Foundation)     |
| HTML                 |
| EJS					|
| jQuery               |
| Node.JS              |
| EXPRESS              |
| PostgreSQL           |
| Knex                 |
| Bcrypt			   |
| Passport/LinkedIn OAuth2 |
 

| APIs Consumed   |
| --------------- |
| INDEED.COM      |

##Screenshots
###### Home Page (No login required)
![alt tag](https://github.com/ono760/Job_Chaser/blob/master/public/images/screenshots/home_no_login.png)
