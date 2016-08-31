
# Markovify Random Text Generator
####Link: [Markovify](https://q3-project.herokuapp.com/)
***

This web application is a Python implementation of a Markov text generator. This application was built in collaboration with @superkun2010. 

>**Markov Model**: "A sequence of possible events in which the probability of each event only depends on the state attained in the previous event."

This text generator can be used to randomly generate somewhat realistic sentences. The application starts with two consecutive words from the text. The last two words constitute the current state. Generating the next word is the Markov transition because the next word depends on the current state. The program then randomly picks one word from a statistical model of the text corpus.


Our current models are created using large corpora of texts from speeches and tweets by Donald Trump and Barack Obama. Users can also enter their own text. For sentiment analysis, we used Python's NLTK (Natural Language Toolkit) to generate random positive or negative sentences from the original input text. The larger text corpora you choose, the more choices the program will have for each transition and a better looking text will be generated. 




|Technologies Used   |
| -------------------- |
| Python 2.7    		  	|
| HTML                 |
| Flask					|
| Markov Library         |
| Natural Language Toolkit (NLTK)|
 

| APIs Consumed   |
| --------------- |
| Twitter.com      |


##Screenshots
###### Home Page
![alt tag](https://github.com/ono760/Job_Chaser/blob/master/public/images/home_screen.png)