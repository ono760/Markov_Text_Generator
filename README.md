# Markov Text Generator
####[Try it out!](https://gentext.herokuapp.com/)
***

This application was built in collaboration with @superkun2010. 

>**Markov Model**: "A sequence of possible events in which the probability of each event only depends on the state attained in the previous event."

This text generator can be used to randomly generate natural-like sentences. The application starts with two consecutive words from the text. The last two words constitute the current state. Generating the next word is the Markov transition because the next word depends on the current state. The program then randomly picks one word from a statistical model of the text corpus. 

Our current models are created using large corpora of texts from speeches and tweets by Donald Trump and Barack Obama. Users can also input their own text. 

For sentiment analysis, we implemented Python's NLTK (Natural Language Toolkit) to assign a polarity score to words ranging from 0 (negative) to 1 (positive) in order to filter text and generate random sentences from the original input text. 

The larger the text corpora you choose is, the more choices the program will have for each transition and a better natural-like text will be generated. 





|Technologies Used   |
| -------------------- |
| Python 2.7    		  	|
| Flask                 |
| HTML5					|
| CSS3         |
| Natural Language Toolkit (NLTK)|
 

| APIs Consumed   |
| --------------- |
| Twitter.com      |


##Screenshots
###### Home Page
![alt tag](https://github.com/ono760/Q3_Project/blob/master/assets/images/home_page.png)
###### Trump Text
![alt tag](https://github.com/ono760/Q3_Project/blob/master/assets/images/trump.png)
###### Obama Text
![alt tag](https://github.com/ono760/Q3_Project/blob/master/assets/images/obama.png)

